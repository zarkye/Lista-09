def dobro_das_pares_triplo_das_impares_posicoes(lista) -> list:
    resultado = []
    for i, n in enumerate(lista):
        if i % 2 == 0:
            resultado.append(n * 2)
        else:
            resultado.append(n * 3)

    return resultado
