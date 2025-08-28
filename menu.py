lista_usuarios = {}


class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade 
    
    def exibir_usuarios(self):
        return f"Usuário: {self.nome} | Email: {self.email} | Idade: {self.idade}"

    

def novo_usuario(nome, email, idade):
    if email not in lista_usuarios:
        lista_usuarios[email] = Usuario(nome, email, idade)
        print("Usuário adicionado com sucesso")
    else:
        print("Email ja cadastrado!")
    


def pesquisar_usuario(email):
    if email in lista_usuarios:
        print(lista_usuarios[email])