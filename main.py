from dotenv import load_dotenv
import os
from pathlib import Path
import requests


def load_env():
    dotenv_path = Path('./network/api_env.env')
    load_dotenv(dotenv_path=dotenv_path)

def display_weather(data):
    print("\nWeather Data:")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Description: {data['weather'][0]['description'].capitalize()}")

def get_weather(city, units="metric"):
    base_url = os.getenv('BASE_URL')
    api_key = os.getenv('API_KEY')

    print(base_url)
    
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : units
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        display_weather(data)
        

load_env()
while True:
    print('Enter exit to close the application')
    city = input('Enter your city name: ')
    if city.lower() == 'exit':
        break
    get_weather(city)