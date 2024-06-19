def obter_resultado_vendas(vendedores: dict) -> dict:
    media = sum(vendedores.values()) / len(vendedores)
    pessoas_abaixo_da_media = []
    pessoas_acima_da_media = []
    for (nome, valor) in vendedores.items():
        if valor < media:
            pessoas_abaixo_da_media.append(nome)
        elif valor > media:
            pessoas_acima_da_media.append(nome)

    return {
        "acima_da_media": pessoas_acima_da_media,
        "abaixo_da_media": pessoas_abaixo_da_media
    }








