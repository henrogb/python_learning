produtos = []

class Produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def calcular_estoque(self):
        return self.preço * self.quantidade
    
    def __str__(self):
       return f"{self.nome} - Preço: {self.preço} - Quantidade: {self.quantidade}."


def novo(nome, preço, quantidade):
    for p in produtos:
        if p.nome == nome:
            print("esse porduto ja existe")
            return
    produtos.append(Produto(nome, preço, quantidade))

novo("henro", 5.98, 9)
novo("henro", 5.98, 9)

for i in produtos:
    print(i.__str__())



