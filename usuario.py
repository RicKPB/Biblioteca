class Usuario():
    def __init__(self, nome, email, senha, administrador) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha
        self.administrador = bool(administrador)