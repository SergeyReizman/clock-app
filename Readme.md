⏰ Digital Clock App (Flask 3.0.3)

A modern, visually engaging digital clock built with Flask 3.0.3 and vanilla JavaScript. Features include a rainbow animated gradient, neon glow effects, glassmorphism UI, and a fully responsive design. The clock updates every second using a lightweight backend API endpoint.

Now with automatic deployment to PythonAnywhere via GitHub Actions, every push to main updates the live app instantly! 🌈✨

✨ Features

Live Digital Clock — updates every second in real time

Rainbow Animated Gradient — smooth, dynamic background transitions 🌈

Neon Glow Effects — animated glowing text on the clock

Glassmorphism UI — frosted-glass container with blur and inset shadows

Responsive Design — optimized for desktop, tablet, and mobile

Simple API Endpoint — /time returns the current server time

Lightweight & Fast — no external JS libraries required

CI/CD Ready — auto-deploy to PythonAnywhere via GitHub Actions

🚀 Quick Start
Prerequisites

Python 3.7+

pip installed

Installation
git clone <your-repo-url>
cd clock-app
pip install -r requirements.txt

Run Locally
python app.py


Open in your browser:
http://127.0.0.1:5000

📁 Project Structure
clock-app/
│
├── app.py                 # Flask application
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
│
├── templates/
│   └── index.html         # Main HTML template
│
└── static/
    └── style.css          # Rainbow gradient + neon glow CSS

🛠️ Technical Overview

Backend (Flask)

Flask 3.0.3

/ → serves HTML template

/time → returns current server time (HH:MM:SS)

Frontend

Vanilla JavaScript fetches /time every second

CSS animations for rainbow glow effects using text-shadow and @keyframes

Glassmorphism using backdrop-filter: blur(10px)

Fully responsive using media queries for tablet and mobile

No frontend frameworks required

🔌 API Endpoints
Endpoint	Method	Description
/	GET	Serves the clock webpage
/time	GET	Returns the current time

Example Response:

14:32:07

🎨 Customization

Change Background Gradient — edit in static/style.css:

background: linear-gradient(135deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #8f00ff);


Edit Glow Color — modify text-shadow inside #clock:

text-shadow: 0 0 10px #ff00ff, 0 0 20px #00e5ff, 0 0 40px #ffff00;


Adjust Animation Speed:

animation: rainbowGlow 3s ease-in-out infinite alternate;


Container Style:

backdrop-filter: blur(12px);
border-radius: 25px;

🌐 Deployment

Recommended Platform: PythonAnywhere

Upload project files

Install requirements: pip install -r requirements.txt

Configure WSGI path

Reload web app → live rainbow digital clock

Other Platforms:

Heroku

AWS Elastic Beanstalk

DigitalOcean App Platform

Railway

Render.com

🐛 Troubleshooting

CSS Not Loading: Ensure correct path in index.html:

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


Time Not Updating: Ensure /time route returns plain text:

return datetime.now().strftime("%H:%M:%S")


PythonAnywhere Errors: Check WSGI file path and reload the web app

🤝 Contributing

Pull requests are welcome!

Fork the repo

Create your feature branch

Commit changes

Open a pull request

📝 License

This project is open source and available under the MIT License

✅ Pro Tip: The repo now includes GitHub Actions → PythonAnywhere API auto-deploy workflow. Every push to main updates the live web app instantly — no manual uploads required!