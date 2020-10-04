# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route('/')
def home():
    return render_template("map.html")

@app.route('/heatmap')
def heat():
    return render_template("heatmap.html")

# create route that renders index.html template
@app.route('/documentation')
def documentation():
    return render_template("documentation.html")

if __name__ == "__main__":
    app.run()
