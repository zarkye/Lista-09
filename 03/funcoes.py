def transformar_lista(lista: list) -> list:
    resultado = []
    for i, n in enumerate(lista):
        if i == 0:
            if n % 2 == 0:
                resultado.append(n + 2)
            else:
                resultado.append(n - 1)
        elif n % 2 == 0:
            lista.append(n + lista[i - 1])
        else:
            resultado.append(lista[n] - lista[n - 1])

    return resultado


def obter_valor(atual: int, anterior: int) -> int:
    if atual % 2 == 0:
        return atual + anterior
    return atual - anterior
