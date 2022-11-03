import requests

city_name = input("Enter a city name (US Only): ")

request = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},US&appid=40c87dc6bc79464a367a089991c33997"
response = requests.get(request).json()

city_lat = response[0]['lat']
city_lon = response[0]['lon']

request2 = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid=40c87dc6bc79464a367a089991c33997&units=metric"
response2 = requests.get(request2).json()

weather_description = response2['weather'][0]['description']
temperature = response2['main']['temp']

print(f"\n{city_name} Weather Conditions:\nDescription: {weather_description}\nTemperature: {temperature}")
