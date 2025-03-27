from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/carousel')
def carousel():
    return render_template('carousel.html', campaigns=campaigns, comma_num = to_string)

def to_string(num):
    return f'{num:,}'

if __name__ == '__main__':
    app.run(debug=True)