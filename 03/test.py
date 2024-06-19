from funcoes import *


def test_verificar_funcao_posicao_anterior():
    resultado = transformar_lista([10, 8, 12, 9, 20])
    assert resultado == [14, 22, 34, -25, -5]
