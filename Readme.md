# ⏰ Digital Clock App (Flask 3.0.3)

A modern, visually engaging digital clock built with **Flask 3.0.3** and vanilla JavaScript. Features include a rainbow animated gradient, neon glow animations, glassmorphism effects, and a fully responsive design. The clock updates every second using a lightweight backend API endpoint.

---

## ✨ Features

- **Live Digital Clock** — updates every second in real time.  
- **Rainbow Animated Gradient** — smooth background transitions for a dynamic look 🌈.  
- **Neon Glow Effects** — animated glowing text on the clock.  
- **Glassmorphism UI** — frosted-glass container with blur and inset shadows.  
- **Responsive Design** — optimized for desktop, tablet, and mobile.  
- **Simple API Endpoint** — `/time` returns the current server time.  
- **Lightweight & Fast** — no external JavaScript libraries or frameworks required.  

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- `pip` installed

### Installation

```bash
git clone <your-repo-url>
cd clock-app
pip install -r requirements.txt
Run Locally
bash
Копировать код
python app.py
Open in your browser:

cpp
Копировать код
http://127.0.0.1:5000
📁 Project Structure
powershell
Копировать код
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

/ → serves the HTML template

/time → returns current server time in HH:MM:SS format

Frontend
Vanilla JavaScript fetches /time every second

CSS animations for rainbow glow effects using text-shadow and @keyframes

Glassmorphism with backdrop-filter: blur(10px)

Fully responsive using media queries for tablet and mobile

No frontend frameworks required

🔌 API Endpoints
Endpoint	Method	Description
/	GET	Serves the clock webpage
/time	GET	Returns the current time

Example Response:

makefile
Копировать код
14:32:07
🎨 Customization
Change Background Gradient
Edit in static/style.css:

css
Копировать код
background: linear-gradient(135deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #8f00ff);
Edit Glow Color
Modify text-shadow inside #clock:

css
Копировать код
text-shadow: 0 0 10px #ff00ff, 0 0 20px #00e5ff, 0 0 40px #ffff00;
Adjust Animation Speed
css
Копировать код
animation: rainbowGlow 3s ease-in-out infinite alternate;
Container Style
css
Копировать код
backdrop-filter: blur(12px);
border-radius: 25px;
🌐 Deployment
Recommended Platform: PythonAnywhere
Upload project files.

Install requirements: pip install -r requirements.txt.

Configure WSGI path.

Reload the web app → live rainbow digital clock.

Other Platforms
Heroku

AWS Elastic Beanstalk

DigitalOcean App Platform

Railway

Render.com

🐛 Troubleshooting
CSS Not Loading: Ensure correct path in index.html:

html
Копировать код
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
Time Not Updating: Ensure /time route returns plain text:

python
Копировать код
return datetime.now().strftime("%H:%M:%S")
PythonAnywhere Errors: Check WSGI file path and reload the web app.

🤝 Contributing
Pull requests are welcome!

Fork the repo, create your feature branch, commit changes, and open a pull request.

📝 License
This project is open source and available under the MIT License.