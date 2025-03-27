from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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

@app.route('/create/submit', methods=['POST'])
def create_campaign():
    data = request.form
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)