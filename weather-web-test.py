from flask import Flask, render_template, request    
import requests 
# redirect, url_for, json
app = Flask(__name__)

my_API_key = ""

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # return render_template('index.html', content = info(request.form.get('cityName')))
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        if latitude and longitude:
            content = info(latitude, longitude);

        else:
            content = '<p>Please select a location on the map...</p>';

        return render_template('index.html', content = content);
    else:
        return render_template('index.html', content = '')

def info(latitude, longitude):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={my_API_key}')
    details = response.json()
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
