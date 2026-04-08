import tkinter as tk

from interface.handlers import iniciar, lembrar, beber_agua, parar

# Criar janela principal do programa, além de configurar ela e manter aberta e demais coisas
def criar_app():
    janela = tk.Tk()
    janela.title("lembrete de água")
    janela.geometry("500x400")

    # Definindo input para META DIÁRIA de água

    label_meta = tk.Label(janela, text="Meta diária(ml)")
    label_meta.pack()

    input_meta = tk.Entry(janela)
    input_meta.pack()

    # Definindo o input para o INTERVALO entre um copo e outro
    label_intervalo = tk.Label(janela, text="Intervalo (min):")
    label_intervalo.pack()

    input_intervalo = tk.Entry(janela)
    input_intervalo.pack()

    # Definindo input para a QUANTIDADE que foi consumido de água
    label_consumo = tk.Label(janela, text="Quanto você bebeu (ml):")
    label_consumo.pack()

    input_consumo = tk.Entry(janela)
    input_consumo.pack()

    # Barra de progresso
    from tkinter import ttk

    barra_progresso = ttk.Progressbar(janela, length=200, mode='determinate')
    barra_progresso.pack(pady=10)

    label_progresso = tk.Label(janela, text="0 / 0 ml")
    label_progresso.pack()

    # Mensagem na tela de para erro/sucesso
    label_mensagem = tk.Label(janela, text="", fg="red")
    label_mensagem.pack(pady=5)

    # Botão de iniciar

    botao = tk.Button(
        janela,
        text="Iniciar",
        command=lambda: iniciar(
            janela,
            input_meta,
            input_intervalo,
            label_mensagem,
            lembrar
        )
    )
    botao.pack(pady=10)

    # Botão de beber água
    botao_beber = tk.Button(
        janela,
        text="Bebi água",
        command=lambda: beber_agua(
            label_mensagem,
            input_consumo,
            barra_progresso,
            label_progresso,
        )
    )
    botao_beber.pack(pady=10)

    # Botão para reiniciar
    botao_parar = tk.Button(
        janela,
        text="Parar",
        command=lambda: parar(label_mensagem)
    )
    botao_parar.pack(pady=10)

    return janela


