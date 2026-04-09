from src.logic.consumo import (
    definir_meta,
    adicionar_consumo,
    calcular_progresso,
    get_consumo,
    get_meta
)


# Função central (regra de negócio)
def test_calcular_progresso():
    definir_meta(1000)
    adicionar_consumo(-get_consumo())  # reset

    adicionar_consumo(500)
    progresso = calcular_progresso()

    assert progresso == 50


# Caso limite (atingiu meta)
def test_meta_atingida():
    definir_meta(1000)
    adicionar_consumo(-get_consumo())  # reset

    adicionar_consumo(1000)
    progresso = calcular_progresso()

    assert progresso == 100


# Entrada inválida
def test_valor_negativo():
    definir_meta(1000)
    adicionar_consumo(-get_consumo())  # reset

    total = adicionar_consumo(-500)

    assert total >= 0


# Validação (meta correta)
def test_definir_meta():
    definir_meta(2000)
    assert get_meta() == 2000
