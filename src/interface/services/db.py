from supabase import create_client
from dotenv import load_dotenv
from src.interface.services.db import get_supabase
import os

load_dotenv()


def get_supabase():
    url = os.getenv("SUPABASE_URL")
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
#funcao