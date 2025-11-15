⏰ Digital Clock App (Flask 3.0.3)

A modern, visually engaging digital clock built with Flask 3.0.3 and vanilla JavaScript, featuring a rainbow animated gradient, neon glow animations, and fully responsive design. The time updates every second using a lightweight backend API endpoint.

✨ Features

Live Digital Clock — updates every second in real time

Rainbow Animated Gradient — smooth background transitions for a dynamic look 🌈

Neon Glow Effects — animated glowing text on the clock

Glassmorphism UI — frosted-glass container with blur and inset shadows

Responsive Design — optimized for desktop, tablet, and mobile

Simple API Endpoint — /time returns the current server time

Lightweight & Fast — no external JS libraries or frameworks required

🚀 Quick Start
Prerequisites

Python 3.7+

pip installed

🔧 Installation

Clone the repository

git clone <your-repo-url>
cd clock-app


Install dependencies

pip install -r requirements.txt


Run the app locally

python app.py


Open in your browser

http://127.0.0.1:5000

📁 Project Structure
clock-app/
│
├── app.py                 # Flask application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── templates/
│   └── index.html         # Main HTML template
│
└── static/
    └── style.css          # Rainbow animated gradient + neon glow CSS

🛠️ Technical Overview
Backend (Flask)

Flask 3.0.3

/ renders the HTML template

/time returns current server time (HH:MM:SS)

Lightweight server-side time generation

Frontend

Vanilla JavaScript fetches /time every second

CSS Rainbow Glow Animations using text-shadow and keyframes

Glassmorphism using backdrop-filter: blur(10px)

Fully responsive with media queries for mobile and tablet

No frontend frameworks required

🔌 API Endpoints
Endpoint	Method	Description
/	GET	Serves the clock webpage
/time	GET	Returns the current time as plain text

Example Response:

14:32:07

🎨 Customization

Change Background Gradient
In static/style.css:

background: linear-gradient(135deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #8f00ff);


Edit Glow Color
Modify text-shadow inside #clock:

text-shadow: 0 0 10px #ff00ff, 0 0 20px #00e5ff, 0 0 40px #ffff00;


Adjust Animation Speed

animation: rainbowGlow 3s ease-in-out infinite alternate;


Container Style

backdrop-filter: blur(12px);
border-radius: 25px;

🌐 Deployment

Recommended Platform: PythonAnywhere

Upload project files

Install requirements

Configure WSGI path

Reload web app → live rainbow digital clock

Other Platforms:

Heroku

AWS Elastic Beanstalk

DigitalOcean App Platform

Railway

Render.com

🐛 Troubleshooting

CSS Not Loading
Use correct path in index.html:

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


Time Not Updating
Ensure /time route returns plain text:

return datetime.now().strftime("%H:%M:%S")


PythonAnywhere Errors
Check the WSGI file path and reload the web app

🤝 Contributing

Pull requests are welcome!

Fork the repo

Create your feature branch

Commit your changes

Open a pull request

📝 License

This project is open source and available under the MIT License.