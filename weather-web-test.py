from flask import Flask
import requests, json

app = Flask(__name__)

my_API_key = "d29ca490f40cf3c78c2e2895f0f3b62c"
city = 'New Jersey' 

# url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_API_key}')
    return response.json()

# def main():
#     city = input("Enter city: ")
#     details = get_weather(city)

    # Print table header
    # print("Weather Details:")
    # print("-----------------")
    # print("City:", details['name'])
    # print("Country:", details['sys']['country'])
    # temperature = details['main']['temp'] - 273.15
    # feels_like = details['main']['feels_like'] - 273.15
    # print(f"Temperature: {temperature:.2f}", "°C")
    # print(f"Feels Like: {feels_like:.2f}", "°C")
    # print("Humidity:", details['main']['humidity'], "%")
    # print("Description:", details['weather'][0]['description'])
    # print("Wind Speed:", details['wind']['speed'], "m/s")
    # print("Cloudiness:", details['clouds']['all'], "%")
    # print("Sunrise:", details['sys']['sunrise'])
    # print("Sunset:", details['sys']['sunset'])
    # print("-----------------")

@app.route("/")
def home():
    details = get_weather(city)
    return f"""
    <h1>Weather Details:</h1>
    <p>City: {details['name']}</p>
    <p>Country: {details['sys']['country']}</p>
    <p>Temperature: {details['main']['temp'] - 273.15:.2f} °C</p>
    <p>Feels Like: {details['main']['feels_like'] - 273.15:.2f} °C</p>
    <p>Humidity: {details['main']['humidity']} %</p>
    <p>Description: {details['weather'][0]['description']}</p>
    <p>Wind Speed: {details['wind']['speed']} m/s</p>
    <p>Cloudiness: {details['clouds']['all']} %</p>
    <p>Sunrise: {details['sys']['sunrise']}</p>
    <p>Sunset: {details['sys']['sunset']}</p>
    """

if __name__ == "__main__":
    app.run()
