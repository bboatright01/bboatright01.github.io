from flask import render_template, request, redirect, flash, url_for, jsonify
from database import app, load_campaigns, load_campaigns_by_id, add_new_campaign, get_db
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath, isfile
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import login
import mysql.connector
from search import index_campaigns
from whoosh.qparser import QueryParser, MultifieldParser, OrGroup
from whoosh.index import open_dir

PICTURE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
IMAGES_FOLDER = join(dirname(realpath(__file__)), 'static/images/') # Full path to the static/images directory

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

def augment_campaigns(campaigns):
    for campaign in campaigns:
        campaign['Raised'] = 10000 # Example data for testing; to be replaced with database
        campaign['Image'] = "default.jpg" # Example data for testing; to be replaced with database
        for extension in PICTURE_EXTENSIONS: #Check if the image file exists in the static/images directory
            if (isfile(IMAGES_FOLDER + str(campaign['id']) + '.' + extension)):
                campaign['Image'] = str(campaign['id']) + '.' + extension
    return campaigns

def get_campaigns():
    campaigns = load_campaigns() # Load campaigns from the database
    campaigns = augment_campaigns(campaigns) # Augment the campaigns with additional data
    return campaigns

index_campaigns(get_campaigns())

@app.route('/')
def home():
    return render_template('home.html', campaigns=get_campaigns(), comma_num = to_string)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create')
def create():
    return render_template('create.html')

#Route for the create campaign page; this will be the form that the user fills out to create a new campaign
@app.route('/create/submit', methods=['POST']) #This will fetch the data from the form
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
        number_filename = number_file(file.filename, new_campaign.lastrowid)
        filename = secure_filename(number_filename)
        path = IMAGES_FOLDER
        file.save(path + filename) # Save the file to the static/images directory
    index_campaigns(get_campaigns()) # Re-index the campaigns after adding a new one
    return render_template('create-submit.html', data=data)
    #return jsonify({"id": new_campaign.lastrowid, **data}) #This will return the data in JSON format; temporary until confirmation page is created

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
            campaigns = load_campaigns_by_id(search_results_ids) # Load campaigns from the database using the IDs from the search results
            campaigns = augment_campaigns(campaigns)
            return render_template('search-results.html', campaigns=campaigns, comma_num = to_string)
            #return jsonify(search_results_ids)
    return render_template('search.html')

# Route for the carousel page; template that enables dynamic display of campaign cards that can connect to database
@app.route('/carousel') 
def carousel():
    return render_template('carousel.html', campaigns=get_campaigns(), comma_num = to_string) # Pass the list of campaigns to the template, as well as the to_string function

@app.route('/donor-login', methods=['GET', 'POST'])
def donor_login():
    form = login.LoginForm()
    print("Form method:", request.method)
    print("Form errors:", form.errors)
    if form.validate_on_submit():
        username = form.username.data
        password_input = form.password.data
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM donors WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        print("Form validated!")
        print("Username:", form.username.data)
        if user and check_password_hash(user['password'], password_input):
            user_obj = login.User(user['id'], user['username'], user['password'])
            login_user(user_obj)
            flash("Login successful", "success")
            return redirect(url_for('donor_dashboard'))
        flash("Invalid credentials", "danger")
    return render_template('donor-login.html', form=form)


@app.route('/donor-registration', methods=['GET', 'POST'])
def donor_registration():
    form = login.RegisterForm()
    print("Form method:", request.method)
    print("Form errors:", form.errors)
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        conn = get_db()
        cursor = conn.cursor()
        print("Form validated!")
        print("Username:", form.username.data)
        try:
            print("Trying to insert into DB...")
            cursor.execute("INSERT INTO donors (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            print("User inserted.")
            flash("User registered!", "success")
            return redirect(url_for('donor_login'))
        except mysql.connector.IntegrityError:
            flash("Username already taken.", "danger")
        except Exception as e:
            print("Error inserting user:", e)
            flash("An error occurred during registration.", "danger")
        finally:
            cursor.close()
            conn.close()
    return render_template('donor-registration.html', form=form)


@app.route('/donor-dashboard')
@login_required
def donor_dashboard():
    return render_template('donor-dashboard.html', user=current_user, campaigns=get_campaigns())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out", "info")
    return redirect(url_for('donor-login'))

if __name__ == '__main__':
    app.run(debug=True)