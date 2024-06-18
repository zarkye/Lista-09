from exercicio import *


def test_extrair_posicao_pares():
    entrada = [10, 15, 2, 21, 37, 4, 9, 13, 20, 31]
    saida = extrair_pares(entrada)
    assert saida == [10, 2, 37, 9, 20]


def test_posicoes_pares_e_impares_dobradas_triplicadas():
    entrada = [5, 10, 9, 2, 1, 20, 40, 8, 33, 42]
    saida = posicoes_pares_e_impares(entrada)
    assert saida == [10, 30, 18, 6, 2, 60, 80, 24, 66, 126]
