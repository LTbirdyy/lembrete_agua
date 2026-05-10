import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = (
    st.secrets.get("API_KEY", None)
    if hasattr(st, "secrets")
    else None
) or os.getenv("API_KEY")
CIDADE = "Brasília"


def pegar_clima():
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
