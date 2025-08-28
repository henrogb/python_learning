def gerador_dict(lista1, lista2):
    dicionario = {}
# {chave: valor for chave, valor in zip(lista1, lista2)} //opção viavel tmb
    for v1, v2 in zip(lista1, lista2):
        dicionario[v1] = v2
    return dicionario


listan = ["nome", "idade"]
listap = ["joao", 20]

print(gerador_dict(listan, listap))
