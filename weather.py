import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather_condition(city = "Ahmedabad"):
    city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={os.getenv("API_KEY")}'
    city_info = requests.get(city_url).json()
    if city_info != []:
        lat = city_info[0]['lat']
        lon = city_info[0]['lon']
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv("API_KEY")}'
        weather_info = requests.get(weather_url).json()

        return weather_info
    else:
        return "none"

if __name__ == "__main__":
    city = input("Enter a city: ")
    a = get_weather_condition(city)
    print(a)

