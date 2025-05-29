# Fetch weather data from OpenWeatherMap API
import requests
import os
from dotenv import load_dotenv

def fetch_weather(city_name, api_key):
    """
    Fetches weather data for a given city from OpenWeatherMap API.

    Args:
        city_name (str): Name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: Weather data as a dictionary, or None if request fails.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("API key not found in .env file.")
        return

    city_name = input("Enter city name: ")
    weather = fetch_weather(city_name, api_key)
    if weather:
        print(f"Weather in {city_name}:")
        print(weather)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()