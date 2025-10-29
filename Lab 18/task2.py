import requests
import json
from requests.exceptions import RequestException, Timeout, ConnectionError

def get_weather(city, api_key='144f322cbb3de167fca196f65fcca129'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }
    
    try:
        # Set timeout to 5 seconds to handle slow connections
        response = requests.get(base_url, params=params, timeout=5)
        
        # Check if the response was successful
        response.raise_for_status()
        
        # Parse the JSON response
        weather_data = response.json()
        
        # Check if the API returned an error message
        if 'cod' in weather_data and weather_data['cod'] != 200:
            print(f"Error: {weather_data.get('message', 'Unknown API error')}")
            return
        
        # Pretty print the JSON data
        print(json.dumps(weather_data, indent=2))

    except Timeout:
        print("Error: Request timed out. Please check your internet connection.")
    
    except ConnectionError:
        print("Error: Could not connect to the server. Please check your internet connection.")
    
    except RequestException as e:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found.")
        else:
            print(f"Error: Could not retrieve weather data. {str(e)}")
    
    except json.JSONDecodeError:
        print("Error: Invalid response from the server.")
    
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

def main():
    try:
        city = input("Enter city name: ")
        if not city.strip():
            print("Error: City name cannot be empty.")
            return
        get_weather(city)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()