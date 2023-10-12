from reserva import Reserva

class Livro:
    def __init__(self, quantidadeTotal, quantidadeReservada) -> None:
        self.quantidadeTotal = int(quantidadeTotal)
        self.quantidadeReservada = int(quantidadeReservada)
        self.reservas = list(Reserva)