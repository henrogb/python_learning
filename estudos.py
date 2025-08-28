agenda = {}

#olha q bacana o agenda aqui faz referencia ao dicionário que vc quer acrescentar, bem interessante
def adicionar_contatos(agenda, nome, telefone, email):
    agenda[nome] = {"Telefone": telefone, "Email": email}

def remover_contato(agenda, nome_procurado):
        if nome_procurado in agenda:
            del agenda[nome_procurado]
        else:
             print('nome não encontrado')

def pesquisar_contato(agenda, nome):
     if nome in agenda:
          
adicionar_contatos(agenda, 'henro', 51983191309, 'henrogb@gmail.com')
adicionar_contatos(agenda, 'maria', 51238392983, 'olokinho@gmail.com')

remover_contato(agenda, 'maria')

# pesquisar_contato(agenda, 'henro')

for i in agenda:
     print(i)