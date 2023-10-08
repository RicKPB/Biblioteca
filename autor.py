from obra import Obra

class Autor():
    def __init__(self, nome, informacoes) -> None:
        self.nome = nome
        self.obras = list(Obra)
        self.informacoes = informacoes