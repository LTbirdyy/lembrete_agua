from supabase import create_client
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()


def get_supabase():

    url = None
    key = None

    # Streamlit Cloud
    try:
        url = st.secrets.get("SUPABASE_URL")
        key = st.secrets.get("SUPABASE_KEY")
    except Exception:
        pass

    # Execução local
    if not url:
        url = os.getenv("SUPABASE_URL")

    if not key:
        key = os.getenv("SUPABASE_KEY")

    return create_client(url, key)


def buscar_historico():

    supabase = get_supabase()

    resposta = (
        supabase
        .table("historico")
        .select("*")
        .order("id", desc=False)
        .execute()
    )

    return resposta.data
