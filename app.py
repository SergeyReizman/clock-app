from flask import Flask, render_template
from datetime import datetime

# ---------------------------------------------
# Initialize the Flask application
# __name__ tells Flask where to look for templates/static files
# ---------------------------------------------
app = Flask(__name__)

# ---------------------------------------------
# Route: Home page ("/")
# This loads and returns the index.html file from the templates folder
# ---------------------------------------------


@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------
# Route: "/time"
# This endpoint returns ONLY the current time as a formatted string.
# It is usually requested via JavaScript every second from index.html.
# ---------------------------------------------
@app.route("/time")
def time():
    # datetime.now() → get current system time
    # strftime("%H:%M:%S") → format as HH:MM:SS
    return datetime.now().strftime("%H:%M:%S")


# ---------------------------------------------
# Start the development server
# Only executes when running app.py directly
# ---------------------------------------------
if __name__ == "__main__":
    # app.run() → by default runs on 127.0.0.1:5000 (local machine)
    app.run()
