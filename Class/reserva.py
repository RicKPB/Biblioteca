from livro import Livro
from usuario import Usuario

class Reserva:
    def __init__(self, codigoReserva) -> None:
        self.codigoReserva = int(codigoReserva)
        self.livro = Livro
        self.portador = Usuario
        self.dataReserva = ...
        self.dataDevolucao = ...