def obter_posicoes_pares(lista) -> list:
    resultado = []
    for i, n in enumerate(lista):
        if i % 2 == 0:
            resultado.append(n)
    return resultado
