import winsound
import os


def tocar_alerta():
    # pega o diretório atual do arquivo alerta.py
    base_dir = os.path.dirname(__file__)

    # monta caminho assim programa é executado em outros maquinas sem problema
    caminho = os.path.join(base_dir, "..", "assets", "sounds", "alerta.wav")
    caminho = os.path.abspath(caminho)

    # toca o som do alerta
    winsound.PlaySound(caminho, winsound.SND_FILENAME | winsound.SND_ASYNC)
