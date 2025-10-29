import requests
import json

def get_weather(city, api_key='144f322cbb3de167fca196f65fcca129'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    # Pretty print the JSON data
    print(json.dumps(weather_data, indent=2))

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)