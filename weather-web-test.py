from flask import Flask, render_template
import datetime
import requests 
# redirect, url_for, json
app = Flask(__name__)

my_API_key = "d29ca490f40cf3c78c2e2895f0f3b62c"
cityName = 'New York'

def get_weather_data(cityName):
    c = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={my_API_key}').json()
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={c['coord']['lat']}&lon={c['coord']['lon']}&appid={my_API_key}')
    details = response.json()
    return details

@app.route("/")
def city_info():
    city_data = get_weather_data(cityName)['city']
    city_data['sunrise'] = datetime.datetime.fromtimestamp(city_data['sunrise'])
    city_data['sunset'] = datetime.datetime.fromtimestamp(city_data['sunset'])
    return render_template("index.html", city=city_data)

@app.route("/forecast")
def forecast():
    forecast = get_weather_data(cityName)['list']
    return render_template('forecast.html', weather_data=forecast)

if __name__ == "__main__":
    app.run(debug=True)
