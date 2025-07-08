import requests

zip_code = input("Please enter your zip code: ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},&appid=a2ad74a539168ed0cd0a45a256805778&units=imperial")

if response:
    response_dictionary = response.json()
    
    city_name = response_dictionary["name"]
    conditions = response_dictionary["weather"][0]["description"]
    temp = round(response_dictionary["main"]["temp"])
    feels_like = round(response_dictionary["main"]["feels_like"])
    humidity = response_dictionary["main"]["humidity"]
    wind_speed = round(response_dictionary["wind"]["speed"])
    wind_direction = response_dictionary["wind"]["deg"]

    print()
    print("Current Weather for ", city_name, ":", sep="")
    print("Conditions:", conditions.title())
    print("Temperature:", temp, "Degrees")      
    print("Feels Like:", feels_like, "Degrees")
    print("Humidity: ", humidity, "%", sep="")        
    print("Wind:", wind_speed, "knots @", wind_direction, "degrees")
    print()