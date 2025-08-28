def claculadora(lista):

    soma = sum(lista)
    print(f'A soma dos numeros é: {soma}')

    media = sum(lista) / len(lista)
    print(f'A media dos numeros é: {media}')

    menor = min(lista)
    print(f'o menor numero é: {menor}')

    maior = max(lista)
    print(f'o maior numero da lista é: {maior}')

lista = [1, 9, 200, 300, 120, 5, 3]

claculadora(lista)