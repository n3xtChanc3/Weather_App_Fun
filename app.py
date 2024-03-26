from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.getenv('API_KEY')  # Get API key from environment variable
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            # Convert temperature from Kelvin to Celsius
            temperature_celsius = data['main']['temp'] - 273.15
            weather = f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {temperature_celsius:.2f}°C"
            return render_template('index.html', weather=weather)
        else:
            return render_template('index.html', weather='City not found')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
