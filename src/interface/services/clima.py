import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CIDADE = "Brasília"


def pegar_temperatura():
    url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": CIDADE,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    # se der erro
    if response.status_code != 200:
        print("Erro na API:", response.text)
        return None

    data = response.json()

    return data["main"]["temp"]
