from obra import Obra

class Editora:
    def __init__(self, nome):
        self.nome = nome
        self.obras = list(Obra())

    def cadastroEditora(self, nome):
        self.nome = nome