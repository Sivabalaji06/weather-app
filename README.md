🌤️ Weather Forecast App
A modern, responsive weather application built using Python (Flask) and the OpenWeather API, featuring a beautiful gradient UI that changes based on weather conditions.
This project demonstrates API integration, REST concepts, frontend design, and backend development — great for a beginner portfolio.
🚀 Features
🌈 Dynamic Gradient UI based on weather (Clear, Clouds, Rain, Snow, Smoke, Thunder, etc.)
🌡 Real-time weather data using OpenWeather REST API
📍 Shows city, temperature, description, humidity, and wind speed
🎨 Clean and modern UI using Bootstrap + Custom CSS
📱 Fully responsive design (desktop + mobile)
⚠️ Error handling for invalid city names / invalid API keys
🔑 Secure API key management using environment variables (.env)
📸 Screenshots
🌈 Gradient UI Example
(Replace the image below with your own screenshot)
screenshots/mumbai.png
Add your screenshot to a folder named /screenshots and reference it here.
🛠️ Tech Stack
Area	Technologies
Backend	Python, Flask
API	OpenWeather REST API
Frontend	HTML, CSS, Bootstrap
Tools	Git, GitHub
Security	python-dotenv for API key
📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# OR
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your API key
Create a .env file in the project root:
OPENWEATHER_API_KEY=your_real_api_key_here
▶️ Run the Application
python3 app.py
Visit:
http://127.0.0.1:5000
🧠 How It Works
User enters a city name
Flask sends a GET request to the OpenWeather API
API returns real-time weather data
Weather category (Clear, Rain, Clouds, etc.) is detected
The UI applies a matching gradient background
Weather values + icons are displayed cleanly
📁 Project Structure
weather-app/
│── app.py
│── requirements.txt
│── .env (not committed)
│── static/
│     └── styles.css
│── templates/
│     └── index.html
│── screenshots/
      └── screenshot.png (optional)
🌐 Deployment
You can deploy this app for free on:
Render
Railway
PythonAnywhere
If you want, I can generate a Deploy Guide (DEPLOY.md) for you.
🙌 About
Created by Siva Balaji
A simple but visually impressive project to showcase API integration and frontend design.