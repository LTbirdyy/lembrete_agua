from datetime import datetime

from src.interface.services.db import get_supabase


# Função para salvar dados do dia
def salvar_dia(consumo, meta):

    hoje = datetime.now().strftime("%d/%m/%Y")

    registro = {
        "data": hoje,
        "consumo": consumo,
        "meta": meta,
        "bateu_meta": consumo >= meta
    }

    supabase = get_supabase()

    supabase.table("historico").insert(registro).execute()