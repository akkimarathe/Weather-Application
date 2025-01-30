import requests

# Function to fetch weather data
def fetch_weather(api_key, location):
    try:
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": location, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        # Extract relevant information
        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc.capitalize()}")
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
    except KeyError:
        print("Invalid response received from the API. Please check your inputs.")

if __name__ == "__main__":
    # Place your API key here
    API_KEY = "b7343ffa5afa28d73364dbb5c021c234"
    
    location = input("Enter a city name to get the weather: ")
    fetch_weather(API_KEY, location)
