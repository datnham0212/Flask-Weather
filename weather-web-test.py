from flask import Flask, render_template    
import requests 
# redirect, url_for, json
app = Flask(__name__)

my_API_key = "d29ca490f40cf3c78c2e2895f0f3b62c"

city = input("Enter city name:")

def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_API_key}')
    return response.json()

@app.route("/")
def home():
    return render_template('index.html', content = info())

def info():
    details = get_weather(city)
    table = f"""
    <table border="1">
        <tr>
            <th colspan="2">Weather Details</th>
        </tr>
        <tr>
            <td>City</td>
            <td>{details['name']}</td>
        </tr>
        <tr>
            <td>Country</td>
            <td>{details['sys']['country']}</td>
        </tr>
        <tr>
            <td>Temperature</td>
            <td>{details['main']['temp'] - 273.15:.2f} °C</td>
        </tr>
        <tr>
            <td>Feels Like</td>
            <td>{details['main']['feels_like'] - 273.15:.2f} °C</td>
        </tr>
        <tr>
            <td>Humidity</td>
            <td>{details['main']['humidity']} %</td>
        </tr>
        <tr>
            <td>Description</td>
            <td>{details['weather'][0]['description']}</td>
        </tr>
        <tr>
            <td>Wind Speed</td>
            <td>{details['wind']['speed']} m/s</td>
        </tr>
        <tr>
            <td>Cloudiness</td>
            <td>{details['clouds']['all']} %</td>
        </tr>
        <tr>
            <td>Sunrise</td>
            <td>{details['sys']['sunrise']}</td>
        </tr>
        <tr>
            <td>Sunset</td>
            <td>{details['sys']['sunset']}</td>
        </tr>
    </table>
    """
    return table


if __name__ == "__main__":
    app.run()
