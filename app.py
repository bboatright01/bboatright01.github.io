import mysql.connector
from flask import Flask, render_template, jsonify, request, redirect, flash, url_for
from flask_login import LoginManager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os

from db_connect import get_db

load_dotenv()
print("Connecting to DB:", os.getenv("DB_NAME"))
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback-key")

# List of dictionaries containing campaign information; to be replaced with database
campaigns = [
    {
        'name': "Clean Water for Oromia",
        'organization': "WaterWorks International",
        'raised': 25000,
        'goal': 50000,
        'image': "Clean_Water_for_Oromia.webp"
    },
    {
        'name': "Bangladesh Resilient Roofs",
        'organization': "Hope Builders",
        'raised': 30000,
        'goal': 50000,
        'image': "Bangladesh_Resilient_Roofs.webp"
    },
    {
        'name': "Amazon Fresh Initiative",
        'organization': "Food For All",
        'raised': 16000,
        'goal': 50000,
        'image': "Amazon_Fresh_Initiative.webp"
    },
    {
        'name': "Rural Homes for Rajasthan",
        'organization': "Hope Builders",
        'raised': 8000,
        'goal': 50000,
        'image': "Rural_Homes_for_Rajasthan.webp"
    },
    {
        'name': "Lamu LifeStream Project",
        'organization': "WaterWorks International",
        'raised': 3000,
        'goal': 50000,
        'image': "Lamu_LifeStream_Project.webp"
    },
    {
        'name': "Salud y Esperanza",
        'organization': "Health Horizons Clinics",
        'raised': 20000,
        'goal': 50000,
        'image': "Salud_y_Esperanza.webp"
    },
    {
        'name': "Indonesia Future Scholars",
        'organization': "Education Empowerment",
        'raised': 10000,
        'goal': 50000,
        'image': "Indonesia_Future_Scholars.webp"
    }
]


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create/submit', methods=['POST']) #This will fetch the data from the form
def create_campaign():
    data = request.form
    return jsonify(data) #This will return the data in JSON format; temporary until database is connected


# Route for the carousel page; template that enables dynamic display of campaign cards that can connect to database
@app.route('/carousel') 
def carousel():
    return render_template('carousel.html', campaigns=campaigns, comma_num = to_string) # Pass the list of campaigns to the template, as well as the to_string function


from donor_login import LoginForm, User, RegisterForm
@app.route('/donor-login', methods=['GET', 'POST'])
def donor_login():
    form = LoginForm()
    print("Form method:", request.method)
    print("Form errors:", form.errors)
    if form.validate_on_submit():
        username = form.username.data
        password_input = form.password.data
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Donor_users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        print("Form validated!")
        print("Username:", form.username.data)
        if user and check_password_hash(user['password'], password_input):
            user_obj = User(user['id'], user['username'], user['password'])
            login_user(user_obj)
            flash("Login successful", "success")
            return redirect(url_for('donor_dashboard'))
        flash("Invalid credentials", "danger")
    return render_template('donor-login.html', form=form)


@app.route('/donor-registration', methods=['GET', 'POST'])
def donor_registration():
    form = RegisterForm()
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
            cursor.execute("INSERT INTO Donor_users (username, password) VALUES (%s, %s)", (username, password))
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
    return render_template('donor-dashboard.html', user=current_user, campaigns=campaigns)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out", "info")
    return redirect(url_for('donor-login'))


@app.route('/test-db')
def test_db():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")  # Simple query
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"DB connected! Server time: {result[0]}"
    except Exception as e:
        return f"DB connection failed: {e}"


# Function to convert numbers to string with commas
def to_string(num): 
    return f'{num:,}'

if __name__ == '__main__':
    app.run(debug=True)