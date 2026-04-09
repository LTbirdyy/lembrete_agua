import os
from logic.historico import salvar_dia


def test_salvar_historico():
    salvar_dia(1000, 2000)

    assert os.path.exists("data/historico.json")
