import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"

    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    results = f"{city}/{country} {local_time} Weather: {temperature} Celsius, {condition}"
    print (results)


if __name__ == "__main__":
    get_weather()
