def extrair_pares(entrada: list) -> list:
    # numeros = [10, 15, 2, 21, 37, 4, 9, 13, 20, 31]
    saida = []
    # for i, n in enumerate(entrada):
    #     if i % 2 == 0:
    #         saida.append(n)
    # return saida
    for i in range(0, len(entrada), 2):
        saida.append(entrada[i])
    return saida


def posicoes_pares_e_impares(entrada: list) -> list:
    saida = []
    for i, n in enumerate(entrada):
        if i % 2 == 0:
            n = i * 2
            saida.append(n)
        elif i % 3 == 0:
            n = i * 3
            saida.append(n)
    return saida
