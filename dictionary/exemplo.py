pessoa = {
    "Nome": "Lucas",
    "E-mail": "lucasfagundesice@gmail.com",
    "Idade": 17
}
print("Chaves em pessoa")
for chave in pessoa:
    print(chave)

print("Valores em pessoa")
for valor in pessoa.values():
    print(valor)

print("Itens em pessoa")
for chave, valor in pessoa.items():
    print(f"Chave: {chave} | Valor: {valor}")
