import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

caminho = os.path.join(BASE_DIR, "data", "historico.json")


# Função para salvar data de cada meta
def salvar_dia(consumo, meta):

    # cria pasta se não existir
    os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)

    # dados do dia
    hoje = datetime.now().strftime("%d/%m/%Y")
    bateu_meta = consumo >= meta

    registro = {
        "data": hoje,
        "consumo": consumo,
        "meta": meta,
        "bateu_meta": bateu_meta
    }

    # ler arquivo existente
    if os.path.exists(caminho):
        with open(caminho, "r") as f:
            dados = json.load(f)
    else:
        dados = []

    # adicionar novo registro
    dados.append(registro)

    # salvar de volta
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)
