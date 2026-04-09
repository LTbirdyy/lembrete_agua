from src.interface import handlers
from src.interface.layout import *
# Adicionar icon


def configurar_icone(janela):
    import os
    base_dir = os.path.dirname(os.path.dirname(__file__))
    caminho = os.path.join(base_dir, "assets", "icon.ico")
    janela.iconbitmap(caminho)


# Função para deixar centralizado em relação ao monitor
def centralizar(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"+{x}+{y}")


# Criar janela principal do programa, além de configurar ela e manter aberta e demais coisas
def criar_app():

    # Caminho pro icone de agua

    janela = tk.Tk()
    configurar_icone(janela)
    janela.title("lembrete de água")
    janela.configure(bg=BG)
    janela.geometry("500x500")

    # Definindo input para META DIÁRIA de água
    criar_label(janela, "Meta diária (ml)").pack(pady=5)
    input_meta = criar_entry(janela)
    input_meta.pack(pady=3)

    # Definindo o input para o INTERVALO entre um copo e outro
    criar_label(janela, "Intervalo (min)").pack(pady=5)
    input_intervalo = criar_entry(janela)
    input_intervalo.pack(pady=3)

    # Definindo input para a QUANTIDADE que foi consumido de água
    criar_label(janela, "Quanto você bebeu (ml)").pack(pady=5)
    input_consumo = criar_entry(janela)
    input_consumo.pack(pady=3)

    # Barra de progresso
    barra = criar_progressbar(janela)
    barra.pack(pady=10)
    label_prog = criar_label(janela, "0 / 0 ml")
    label_prog.pack(pady=4)

    # Mensagem na tela de para erro/sucesso
    label_mensagem = criar_label(janela, "", )
    label_mensagem.pack(pady=5)

    # Botão de iniciar
    btn_iniciar = criar_botao(
        janela,
        "Iniciar",
        lambda: handlers.iniciar(janela, input_meta,
                                 input_intervalo, label_mensagem))

    btn_iniciar.pack(pady=3)

    # Botão de beber água
    btn_agua = criar_botao(
        janela, "Bebi água",
        lambda: handlers.beber_agua(label_mensagem, input_consumo,
                                    barra, label_prog))

    btn_agua.config(bg="#1191b8")
    btn_agua.pack(pady=8)

    # Botão para reiniciar
    btn_parar = criar_botao(
        janela, "Parar",
        lambda: handlers.parar(label_mensagem, barra,
                               label_prog, input_consumo))

    btn_parar.config(bg="#c7200e")
    btn_parar.pack(pady=8)
    centralizar(janela)
    return janela
