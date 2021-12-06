from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def default_home():
     return render_template('home.html')
     
@app.route('/home')
def home():
     return render_template('home.html')

@app.route("/projects")
def projects():
     return render_template('projects.html')

@app.route("/contact")
def contact():
     return render_template('contacts.html')

if __name__=="__main__":
     app.run(debug=True)