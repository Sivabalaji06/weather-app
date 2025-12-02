# app.py
import requests
from flask import Flask, render_template, request
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env if present

app = Flask(__name__)

# prefer environment variable; fallback to hard-coded only for local quick testing
API_KEY = "8fe56b19032663e72b17c2d9099bafaa"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Please enter a city name."
            return render_template("index.html", weather_data=None, error=error)

        city_encoded = urllib.parse.quote_plus(city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={API_KEY}&units=metric"

        print("DEBUG: Requesting URL ->", url)
        try:
            response = requests.get(url, timeout=10)
        except Exception as e:
            print("DEBUG: Request exception ->", e)
            error = "Network error when contacting weather API."
            return render_template("index.html", weather_data=None, error=error)

        print("DEBUG: Status code ->", response.status_code)
        try:
            json_resp = response.json()
            print("DEBUG: Response JSON ->", json_resp)
        except Exception as e:
            print("DEBUG: Could not parse JSON:", e)
            json_resp = {}

        if response.status_code == 200:
            data = json_resp
            # weather[0] exists
            w = data["weather"][0]
            weather_data = {
                "city": data.get("name", city),
                "temperature": round(data["main"]["temp"], 2),
                "description": w.get("description", "").title(),
                "main": w.get("main", ""),     # e.g., "Clear", "Clouds", "Rain"
                "icon": w.get("icon"),         # OpenWeather icon code
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
            }
        elif response.status_code == 401:
            error = "Invalid API key. Check your API_KEY in app.py or .env."
        elif response.status_code == 404:
            error = "City not found. Please try again (spell correctly or try a larger city)."
        elif response.status_code == 429:
            error = "API rate limit reached. Wait a minute and try again."
        else:
            msg = json_resp.get("message") if isinstance(json_resp, dict) else None
            error = f"API error: {msg or 'Unknown error'} (status {response.status_code})"

    return render_template("index.html", weather_data=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
