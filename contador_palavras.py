print("Bem vindo ao seu contador de palavras")
frase = str(input("Digite sua frase: "))

lista = frase.split()

dicionario = {}

for p in lista:
    if p in dicionario:
        dicionario[p] += 1
    else:
        dicionario[p] = 1

for c, v in dicionario.items():
    print(f"{c}: {v}")

    

