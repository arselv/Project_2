from flask import Flask
import function as f

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
