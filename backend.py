import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days, option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    filtered_by_days = filtered_data[:8 * forecast_days]

    if option == "Temperature":
        temperature_data = [item["main"]["temp"] for item in filtered_by_days]
        date_data = [item["dt_txt"] for item in filtered_by_days]
        return temperature_data, date_data
    elif option == "Sky":
        sky_data = [item["weather"][0]["main"] for item in filtered_by_days]
        date_data = [item["dt_txt"] for item in filtered_by_days]
        return sky_data, date_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=2, option="Sky"))