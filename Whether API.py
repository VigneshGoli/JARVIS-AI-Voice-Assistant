import requests

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = '8e4577fce26478246160cb13d4625283'

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={API_KEY}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']

        # Check if precipitation data is available
        if 'rain' in data and '1h' in data['rain']:
            precipitation = data['rain']['1h']
        elif 'snow' in data and '1h' in data['snow']:
            precipitation = data['snow']['1h']
        else:
            precipitation = 0

        # Check for weather condition to estimate the chance of rain
        weather = data['weather'][0]['main']
        if weather == 'Rain':
            chance_of_rain = data['clouds']['all']  # Use cloud cover as an estimate
        else:
            chance_of_rain = 0

        weather_data = {
            "Temperature": temperature,
            "Humidity": humidity,
            "Precipitation": precipitation,
            "Chance of Rainfall (%)": chance_of_rain
        }
        return weather_data
    else:
        return None

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_info = get_weather(city_name)

    if weather_info:
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather_info['Temperature']}°C")
        print(f"Humidity: {weather_info['Humidity']}%")
        print(f"Precipitation (1-hour forecast): {weather_info['Precipitation']} mm")
        print(f"Chance of Rainfall: {weather_info['Chance of Rainfall (%)']}%")
    else:
        print("City not found or API request failed.")
    POP= weather_info['Chance of Rainfall (%)']
k=POP