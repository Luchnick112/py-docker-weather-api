import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    CITI = "Paris"
    BASE_URL = "https://api.weatherapi.com/v1/current.json"
    url = f"{BASE_URL}?q={CITI}&key={api_key}"
    response = requests.get("BASE_URL")
    data = response.json()

    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    results = f"{city}/{country} {local_time} Weather: {temperature} Celsius, {condition}"
    print (results)


if __name__ == "__main__":
    get_weather()
