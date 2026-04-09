from logic.alerta import tocar_alerta
from logic.historico import salvar_dia
from logic.consumo import (
    definir_meta,
    adicionar_consumo,
    calcular_progresso,
    get_consumo,
    get_meta
)

# Variaveis para o estado do sistema
intervalo_ms = 0
rodando = False


def lembrar(janela, label_mensagem):
    global rodando, intervalo_ms
    # Parar o lembrete
    if not rodando:
        return
    label_mensagem.config(text="Hora de beber água", fg="#1191b8")
    tocar_alerta()

    # Chamar a função do som do alerta
    janela.after(intervalo_ms, lambda: lembrar(janela, label_mensagem))


# Função do botão
def iniciar(janela, input_meta, input_intervalo, label_mensagem):
    global intervalo_ms, rodando

    try:
        # pega o valor inputado dentro da janela criada com tkinter
        meta = int(input_meta.get())
        intervalo = int(input_intervalo.get())

        # Caminho em caso de sem erro
        if meta <= 0 or intervalo <= 0:
            label_mensagem.config(text="Valores devem ser maiores que zero!", fg="red")
            return

        # Pega o valor que o user colocou como meta daiira
        definir_meta(meta)

        label_mensagem.config(text="Meta salva!", fg="green")

        # Preciso converte para milisengundos para usar o after() dpo tkinter

        # temp ta em seg pra testar
        intervalo_ms = intervalo * 1000  # minutos -> mili
        rodando = True

        # Iniciando timer
        janela.after(intervalo_ms, lambda: lembrar(janela, label_mensagem))

        print("Meta:", meta)
        print("Intervalo:", intervalo)

    # Mensagem na tela de erro de tipo inválido
    except ValueError:
        label_mensagem.config(text="Insira apenas números", fg="red")


# Função para a quantidade de água ja consumida
def beber_agua(label_mensagem,input_consumo, barra_progresso, label_progresso):
    global rodando
    try:
        quantidade = int(input_consumo.get())

        if quantidade <= 0:
            label_mensagem.config(text="Digite um valor válido!", fg="red")
            return

        total = adicionar_consumo(quantidade)
        progresso = calcular_progresso()

        barra_progresso['value'] = progresso
        label_progresso.config(text=f"{total} / {get_meta()} ml")

        if total == get_meta():
            rodando = False
            barra_progresso['value'] = 100
            label_mensagem.config(text="Parabéns você bateu a meta", fg="green")

            salvar_dia(total, get_meta())
        if total > get_meta():
            label_mensagem.config(text="Muito bem você ultrapassou a meta", fg="purple")

    except ValueError:
        label_mensagem.config(text="Digite apenas números!", fg="red")

def parar(label_mensagem,barra_progresso,label_progresso, input_consumo):
    global rodando
    rodando = False

    consumo = get_consumo()
    meta = get_meta()

    salvar_dia(consumo, meta)
    # Zerar a barra
    barra_progresso['value'] = 0

    # Zerar o texto
    label_progresso.config(text="0 / 0 ml")

    # Limpa o input
    input_consumo.delete(0, 'end')

    label_mensagem.config(text="Intervalo parado e dados salvos", fg="orange")

