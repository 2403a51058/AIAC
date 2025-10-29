import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def get_weather(city, api_key='144f322cbb3de167fca196f65fcca129'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        weather_data = response.json()

        if weather_data.get("cod") != 200:
            print(f"Error: {weather_data.get('message', 'Unknown API error')}")
            return

        # ✅ Extract specific fields
        city_name = weather_data.get("name", "N/A")
        temperature = weather_data.get("main", {}).get("temp", "N/A")
        humidity = weather_data.get("main", {}).get("humidity", "N/A")
        description = weather_data.get("weather", [{}])[0].get("description", "N/A")

        # ✅ Display in user-friendly format
        print("\nWeather Report")
        print(f"• City: {city_name}")
        print(f"• Temperature: {temperature}°C")
        print(f"• Humidity: {humidity}%")
        print(f"• Weather: {description.capitalize()}")

    except Timeout:
        print("Error: Request timed out. Please check your internet connection.")
    except ConnectionError:
        print("Error: Could not connect to the server. Please check your internet connection.")
    except RequestException as e:
        if response.status_code == 401:
            print("Error: Invalid API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found.")
        else:
            print(f"Error: Could not retrieve weather data. {str(e)}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

def main():
    try:
        city = input("Enter city name: ").strip()
        if not city:
            print("Error: City name cannot be empty.")
            return
        get_weather(city)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()