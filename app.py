from flask import Flask, render_template, jsonify, request
from database import load_campaigns, add_new_campaign
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath, isfile
app = Flask(__name__)

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

def get_campaigns():
    campaigns = load_campaigns() # Load campaigns from the database

    for campaign in campaigns:
        campaign['Raised'] = 10000 # Example data for testing; to be replaced with database
        campaign['Image'] = "default.jpg" # Example data for testing; to be replaced with database
        for extension in PICTURE_EXTENSIONS: #Check if the image file exists in the static/images directory
            if (isfile(IMAGES_FOLDER + str(campaign['id']) + '.' + extension)):
                campaign['Image'] = str(campaign['id']) + '.' + extension
    return campaigns

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
    
    return jsonify({"id": new_campaign.lastrowid, **data}) #This will return the data in JSON format; temporary until confirmation page is created

# Route for the carousel page; template that enables dynamic display of campaign cards that can connect to database
@app.route('/carousel') 
def carousel():
    return render_template('carousel.html', campaigns=get_campaigns(), comma_num = to_string) # Pass the list of campaigns to the template, as well as the to_string function

if __name__ == '__main__':
    app.run(debug=True)