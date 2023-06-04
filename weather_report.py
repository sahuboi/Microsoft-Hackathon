import argparse
import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

configure()
API_KEY = os.getenv('api_key')

parser = argparse.ArgumentParser(description="name of city")
parser.add_argument('city', metavar='city', type=str, help='enter the name of city')
args = parser.parse_args()

CITY_NAME = args.city

URL = BASE_URL + "&q=" + CITY_NAME + "&appid=" + API_KEY + "&units=metric"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.HTTPError as err:
    print(err)
else:
    data = response.json()
    temp =  str(data['main']['temp'])
    feel_temp = str(data['main']['feels_like'])
    min_temp = str(data['main']['temp_min'])
    max_temp = str(data['main']['temp_max'])
    pressure = str(data['main']['pressure'])
    humidity = str(data['main']['humidity'])
    visibility = str(data['visibility'])
    wind_spd = str(data['wind']['speed'])
    sky = data['weather'][0]['main']

    # print(response)

    print("Weather in",CITY_NAME+':')
    print("Temperature: "+temp+"°C\n"+"Max. Temperature: "+max_temp+"°C\n"+"Min. Temperature: "+min_temp+"°C\n"+"Feels Like: "+feel_temp+"°C")
    print("Pressure: "+pressure+"N/m^2\n"+"Humidity: "+humidity+"g/m^3")
    print("Visibility: "+visibility+"m\n"+"Wind Speed: "+wind_spd+"m/s\n"+"Sky condition: "+sky)