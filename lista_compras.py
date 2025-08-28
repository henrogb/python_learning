lista_compras = ["banan", "bacon", "mexirica"]
menu = ["1- adicionar item", "2- remover item", "3- itens atuais", "4- sair"]

menu_on = True

print("Ola seja bem vindo a sua lista de compras")

while menu_on:
    for i in menu:
        print(i)

    escolha = int(input("escolha uma das opções a baixo:"))
    match escolha:
        case 1:
            item = input("Qual item gostaria de incluir? ")
            if item in lista_compras:
                print('\n***este item ja existe na lista de compras***\n')
            else:
                lista_compras.append(item)
        case 2:
            remove = input("qual o nome do item a ser removido? ")
            if remove in lista_compras:
                lista_compras.remove(remove)
                print(f"o item {remove}, foi removido com sucesso.")
        case 3:
            print("\n-----------------------------\n")
            index = 0
            for b in lista_compras:
                index += 1
                print(f"{index}. {b}")
                
            print("\n------------------------------\n")    
        case 4: 
            print("saindo...")        
            print("Até logo!")
            menu_on = False