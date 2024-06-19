from funcoes import *


def test_obter_resultado_vendas():
    vendedores = {
        "Joao": 50000,
        "Ana": 65000,
        "Pedro": 72000,
        "Paulo": 4000,
    }

    saida = obter_resultado_vendas(vendedores)

    assert saida["acima_da_media"] == ["Joao", "Ana", "Pedro"]
    assert saida["abaixo_da_media"] == ["Paulo"]
