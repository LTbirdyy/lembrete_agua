# interface/layout.py
import tkinter as tk
from tkinter import ttk
from src.interface.estilo import *

def criar_label(master, texto):
    return tk.Label(master, text=texto, fg=FG, bg=BG, font=FONT_LABEL)


# Cada botão vai ter uma cor, mas fica mais pratico caso queira add novos
def criar_botao(master, texto, comando):
    return tk.Button(master, text=texto, command=comando,
                     bg=BTN_BG, fg=BTN_FG, font=FONT_BTN,
                     padx=10, pady=5)


def criar_entry(master):
    return tk.Entry(master, font=FONT_LABEL, width=25)


def criar_progressbar(master):
    return ttk.Progressbar(master, length=250, mode='determinate')
