from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "App with debug=true"

app.run(debug=True)