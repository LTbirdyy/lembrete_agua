consumo_atual = 0
meta_diaria = 0
def definir_meta(meta):
    global meta_diaria, consumo_atual

    meta_diaria = meta
    consumo_atual = 0

def adicionar_consumo(quantidade):
    global consumo_atual

    # So pra garantir de não colocar que bebu -1 agua
    if quantidade< 0:
        return consumo_atual

    consumo_atual += quantidade
    return consumo_atual

def calcular_progresso():
    if meta_diaria == 0:
        return 0
    return (consumo_atual / meta_diaria) * 100

def get_meta():
    return meta_diaria

# Pegar consumo para poder salvar mesmo se aa pessoa parar antes da meta
def get_consumo():
    return consumo_atual