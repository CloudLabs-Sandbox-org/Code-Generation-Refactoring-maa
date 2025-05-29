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
        print(f"Debug - API URL: {response.url}")
        print(f"Debug - Status Code: {response.status_code}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        if hasattr(e.response, 'text'):
            print(f"Error response: {e.response.text}")
        return None

def main():
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("API key not found in .env file.")
        return
    
    print(f"Debug - Using API key: {api_key}")  # Add this line to verify the key
    
    city_name = input("Enter city name: ")
    weather = fetch_weather(city_name, api_key)
    if weather:
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Conditions: {weather['weather'][0]['description']}")
        print(f"Humidity: {weather['main']['humidity']}%")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()