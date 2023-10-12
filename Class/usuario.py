class Usuario:
    def __init__(self, nome, email, senha, administrador):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.administrador = bool(administrador)

    def adicionarUsuario(self):
        self.nome = input('Digite o nome: ')
        self.email = input('Digite o email: ')
        self.senha = input('Digite o senha: ')
        
        