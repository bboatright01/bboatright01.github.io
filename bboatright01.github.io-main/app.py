from flask import Flask, render_template, request, redirect, flash, url_for, jsonify, session
from werkzeug.utils import secure_filename
from functools import wraps
from os.path import join, dirname, realpath, isfile
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from whoosh.qparser import QueryParser, MultifieldParser, OrGroup
from whoosh.index import open_dir
import requests
import json
import datetime

from login import User, Donor, NGO, load_user, RegisterForm, LoginForm, Subscription
from search import index_campaigns
from database import get_db_url, get_db_engine
from campaigns import load_campaigns, load_campaigns_by_id, add_new_campaign, get_campaigns, augment_campaigns, Campaign
from donations import count_donations_by_unique_id, total_donated_for_campaign
from ngos import get_ngo_by_id
from app_factory import app, db, engine


PICTURE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
IMAGES_FOLDER = join(dirname(realpath(__file__)), 'static/images/')  # Full path to the static/images directory

# Email notification function
def send_notification_email(user_id, username, campaign_id, campaign_name):
    print("Attempting to send email notification...")
    
    # Mailtrap Sandbox API endpoint and bearer token
    url = "https://sandbox.api.mailtrap.io/api/send/3630609"
    bearer_token = "e943c36f37910e9933bd7aea9785d3e1"
    
    # Prepares the email payload
    payload = {
        "from": {
            "email": "changechange743@gmail.com",
            "name": "Change4Change"
        },
        "to": [
            {"email": "changechange743@gmail.com"}
        ],
        "subject": "New Campaign Subscription Alert",
        "text": f"""
        New Subscription Alert!
        
        User {username} (ID: {user_id}) has subscribed to campaign '{campaign_name}' (ID: {campaign_id}).
        
        Subscription Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        This is an automated message from Change 4 Change platform.
        """,
        "category": "Subscription Notification"
    }
    
    # Prepares the headers with the bearer token
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    try:
        print("Sending request to Mailtrap API...")
        print(f"URL: {url}")
        print(f"Headers: {headers}")
        print(f"Payload: {json.dumps(payload)}")
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")
        
        if response.status_code == 200:
            print("Email notification sent successfully to Mailtrap!")
            return True
        else:
            print(f"Failed to send email: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Exception occurred while sending email: {e}")
        return False

# Check if file type is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in PICTURE_EXTENSIONS


# Function to rename the file with the campaign ID and original extension
def number_file(filename, id):
    return str(id) + '.' + filename.rsplit('.', 1)[1].lower()


# Function to get the file number from the filename
def get_file_number(filename):
    return filename.split('.')[0]


# Function to convert numbers to string with commas
def to_string(num): 
    return f'{num:,}'


with app.app_context():
    from campaigns import load_campaigns
    from search import index_campaigns

    index_campaigns(load_campaigns())

@app.route('/')
def home():
    return render_template('home.html', campaigns=get_campaigns(PICTURE_EXTENSIONS, IMAGES_FOLDER), comma_num = to_string)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query_string = request.form.get('search-query')
        index = open_dir("search_index")
        terms = query_string.split()
        query_parser = MultifieldParser(["name", "country", "description"], index.schema, group=OrGroup)
        query = query_parser.parse(" OR ".join(terms))
        with index.searcher() as searcher:
            results = searcher.search(query)
            search_results_ids = [{"id": int(result["id"])} for result in results]
            # Load campaigns from the database using the IDs from the search results
            campaigns = load_campaigns_by_id(search_results_ids)
            campaigns = augment_campaigns(campaigns, PICTURE_EXTENSIONS, IMAGES_FOLDER)
            return render_template('search-results.html', campaigns=campaigns, comma_num = to_string)
            # return jsonify(search_results_ids)
    return render_template('search.html')

# Route for the carousel page; template that enables dynamic display of campaign cards that can connect to database
@app.route('/carousel') 
def carousel():
    # Pass the list of campaigns to the template, as well as the to_string function
    return render_template('carousel.html', campaigns=get_campaigns(), comma_num = to_string)

# Route for campaign details - redirects to the main campaign_detail route
@app.route('/campaigns/<int:campaign_id>')
def campaign(campaign_id):
    # Redirect to the consolidated campaign_detail route
    return redirect(url_for('campaign_detail', campaign_id=campaign_id))


@app.route('/donor-login', methods=['GET', 'POST'])
def donor_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password_input = form.password.data

        # Look up the user in the database
        user = Donor.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password_input):
            login_user(user)  # `user` is already a UserMixin object
            flash("Login successful", "success")
            return redirect(url_for('donor_dashboard'))

        flash("Invalid credentials", "danger")

    return render_template('donor-login.html', form=form)


@app.route('/ngo-login', methods=['GET', 'POST'])
def ngo_login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        ngo = NGO.query.filter_by(username=username).first()
        if ngo and check_password_hash(ngo.password, password):
            session['ngo_id'] = ngo.id
            session['ngo_name'] = ngo.name
            flash("NGO login successful!", "success")
            return redirect(url_for('ngo_dashboard'))

        flash("Invalid credentials", "danger")

    return render_template('ngo-login.html', form=form)


def ngo_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'ngo_id' not in session:
            flash("Please log in as an NGO to access this page.", "warning")
            return redirect(url_for('ngo_login'))
        return f(*args, **kwargs)
    return decorated_function


# Route for the create campaign page; this will be the form that the user fills out to create a new campaign
@app.route('/create/submit', methods=['POST']) #This will fetch the data from the form
@ngo_login_required
def create_campaign():
    if 'file' not in request.files:
        return 'No file part in the request', 400
    file = request.files['file']
    filename = "default.jpg" # Default image if no file is selected
    if file and not allowed_file(file.filename):
        return 'File type must be of type png, jpg, jpeg, gif, or webp', 400
    data = request.form
    if not data['funding-goal'].isdigit():
        return 'Funding goal must be a number', 400
    new_campaign = add_new_campaign(data) # Add the new campaign to the database and return the entry
    if file:
        number_filename = number_file(file.filename, new_campaign.id)
        filename = secure_filename(number_filename)
        path = IMAGES_FOLDER
        file.save(path + filename) # Save the file to the static/images directory
    index_campaigns(get_campaigns(PICTURE_EXTENSIONS, IMAGES_FOLDER)) # Re-index the campaigns after adding a new one
    return render_template('create-submit.html', data=data)


@app.route('/donor-registration', methods=['GET', 'POST'])
def donor_registration():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password_hash = generate_password_hash(form.password.data)
        name = form.name.data

        print("Form validated!")
        print("Username:", username)

        try:
            # Check if username already exists
            if Donor.query.filter_by(username=username).first():
                flash("Username already taken.", "danger")
            else:
                new_donor = Donor(username=username, password=password_hash, name=name)
                db.session.add(new_donor)
                db.session.commit()
                print("User inserted.")
                flash("User registered!", "success")
                return redirect(url_for('donor_login'))

        except Exception as e:
            print("Error inserting user:", e)
            flash("An error occurred during registration.", "danger")

    return render_template('donor-registration.html', form=form)


@app.route('/donor-dashboard')
@login_required
def donor_dashboard():
    subscription_campaign_ids = [s.campaign_id for s in Subscription.query.filter_by(donor_id=current_user.id).all()]
    campaigns = Campaign.query.filter(Campaign.id.in_(subscription_campaign_ids)).all()
    return render_template('donor-dashboard.html', user=current_user, campaigns=campaigns)


@app.route('/ngo-dashboard')
@ngo_login_required
def ngo_dashboard():
    ngo_id = session.get('ngo_id')
    if not ngo_id:
        flash("Please log in as an NGO to access the dashboard.", "warning")
        return redirect(url_for('ngo_login'))

    ngo = NGO.query.get(ngo_id)
    campaigns = Campaign.query.filter_by(NGO_ID=ngo.id).all()

    return render_template('ngo-dashboard.html', user=ngo, campaigns=campaigns)


# Main consolidated route for campaign details
@app.route('/campaign/<int:campaign_id>')
def campaign_detail(campaign_id):
    # Try to get campaign data from the database using load_campaigns_by_id
    campaign_data = load_campaigns_by_id([{"id": campaign_id}])
    
    if not campaign_data:
        # If that fails, try to get the campaign using the ORM
        campaign = Campaign.query.get_or_404(campaign_id)
        # Then we'd need to convert it to the format expected by the template
    else:
        # If we got data from load_campaigns_by_id, augment it and use it
        campaign_data = augment_campaigns(campaign_data, PICTURE_EXTENSIONS, IMAGES_FOLDER)
        campaign = campaign_data[0]
        
    # Get additional data needed for the template
    donor_count = count_donations_by_unique_id(campaign_id)
    total_donated = int(total_donated_for_campaign(campaign_id))
    
    try:
        # Get NGO info if available
        NGO_name = get_ngo_by_id(campaign['NGO_ID'])['Name']
        NGO_description = get_ngo_by_id(campaign['NGO_ID'])['Description']
    except:
        # Default values if NGO info can't be retrieved
        NGO_name = "Unknown Organization"
        NGO_description = "No description available."
    
    # Check subscription status
    is_subscribed = False
    if current_user.is_authenticated:
        is_subscribed = Subscription.query.filter_by(
            donor_id=current_user.id,
            campaign_id=campaign_id
        ).first() is not None
    
    # Render the contact.html template which has all the campaign detail functionality
    return render_template('contact.html', 
                          campaign=campaign, 
                          donor_count=donor_count,
                          total_donated=total_donated, 
                          NGO_name=NGO_name,
                          NGO_description=NGO_description,
                          is_subscribed=is_subscribed)


@app.route('/subscribe/<int:campaign_id>', methods=['POST'])
@login_required
def subscribe(campaign_id):
    existing = Subscription.query.filter_by(
        donor_id=current_user.id,
        campaign_id=campaign_id
    ).first()

    if not existing:
        new_sub = Subscription(donor_id=current_user.id, campaign_id=campaign_id)
        db.session.add(new_sub)
        db.session.commit()
        flash("You are now subscribed!", "success")
        
        # Get campaign details for the email
        campaign_data = load_campaigns_by_id([{"id": campaign_id}])
        if campaign_data:
            campaign_name = campaign_data[0]['Name']
        else:
            campaign = Campaign.query.get_or_404(campaign_id)
            campaign_name = campaign.Name
        
        # Send email notification
        send_notification_email(
            current_user.id, 
            current_user.username, 
            campaign_id, 
            campaign_name
        )
    else:
        flash("You're already subscribed.", "info")

    return redirect(url_for('campaign_detail', campaign_id=campaign_id))


@app.route('/unsubscribe/<int:campaign_id>', methods=['POST'])
@login_required
def unsubscribe(campaign_id):
    sub = Subscription.query.filter_by(
        donor_id=current_user.id,
        campaign_id=campaign_id
    ).first()

    if sub:
        db.session.delete(sub)
        db.session.commit()
        flash("You have unsubscribed from this campaign.", "info")
    else:
        flash("You're not subscribed to this campaign.", "warning")

    return redirect(url_for('campaign_detail', campaign_id=campaign_id))

# Navigation for website
@app.route('/ngoprofile')
@login_required
def ngo_profile():
    return render_template('ngoprofile.html', user=current_user)

@app.route('/postedcampaigns')
@login_required
def posted_campaigns():
    return render_template('postedcampaigns.html', user=current_user, campaigns=get_campaigns())

@app.route('/donations')
@login_required
def donations():
    return render_template('donations.html', user=current_user, campaigns=get_campaigns())

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/logout')
def logout():
    # Log out donor if logged in
    if current_user.is_authenticated:
        logout_user()

    # Log out NGO if logged in
    if 'ngo_id' in session:
        session.pop('ngo_id', None)
        session.pop('ngo_name', None)

    flash("Logged out", "info")
    return redirect(url_for('home'))  # Or to donor-login, if you prefer


if __name__ == '__main__':
    app.run(debug=True)