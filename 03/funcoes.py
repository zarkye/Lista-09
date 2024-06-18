def somar_2_caso_valor_for_par_posicao_anterior(lista) -> list:
    resultado = []

    for posicao, valor in enumerate(lista):
        if lista[posicao] % 2 == 0:
            if posicao == 0 and valor % 2 == 0:
                resultado.append(lista[posicao] + 2)
            else:
                resultado.append(lista[posicao] + lista[posicao - 1])
        else:
            if posicao == 0 and valor % 2 != 0:
                resultado.append(lista[valor] - 1)
            else:
                resultado.append(lista[valor] - lista[valor - 1])

    return resultado


