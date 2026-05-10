import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

CIDADE = "Brasília"


def pegar_clima():
    # pegar API key de forma segura
    API_KEY = None

    try:
        API_KEY = st.secrets.get("API_KEY")
    except Exception:
        pass

    if not API_KEY:
        API_KEY = os.getenv("API_KEY", "fake_key")

    url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": CIDADE,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temp": data["main"]["temp"],
        "cidade": data["name"],
        "sensacao": data["main"]["feels_like"],
        "umidade": data["main"]["humidity"],
        "descricao": data["weather"][0]["description"],
        "vento": data["wind"]["speed"]
    }