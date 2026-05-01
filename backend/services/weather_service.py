import os
import requests


MOCK_WEATHER = {
    "new york": {"weather": "cold", "temperature_c": 9},
    "miami": {"weather": "hot", "temperature_c": 29},
    "seattle": {"weather": "rainy", "temperature_c": 12},
}


def get_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY", "")
    if api_key:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        weather_main = data["weather"][0]["main"].lower()
        weather = "rainy" if "rain" in weather_main else ("hot" if data["main"]["temp"] > 22 else "cold")
        return {"city": city, "weather": weather, "temperature_c": data["main"]["temp"]}

    base = MOCK_WEATHER.get(city.lower(), {"weather": "calm", "temperature_c": 20})
    return {"city": city, **base}
