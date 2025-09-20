import requests
import json

city = input("Enter city name: ")
url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"Bengaluru","lang":"EN"}

headers = {
	"x-rapidapi-key": "819adf7c6dmshb4699a727b2e379p1d02f3jsndd864417541e",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(json.dumps(response.json(), indent=4))