#       ARQUIVO PARA A CRIACAO DE CLASSES PARA O SISTEMA






#----------------------------------------------------
#                       AUTOR

class Autor:
    def __init__(self, nome, informacoes) -> None:
        self.nome = nome
        self.obras = [Obra]
        self.informacoes = informacoes

    
    def cadastroAutor(self):
        self.nome = input('Nome: ')
    
    def cadastroInformacoes(self,):
        self.informacoes = input('Informacoes: ')
    
    def adicionarObra(self, obra):
        self.obras.append(obra)


#----------------------------------------------------
#                CONTROLADOR DE LIVROS

class ControladorLivros:
    def __init__(self) -> None:
        self.livros = [Livro]

#----------------------------------------------------
#                       EDITORA

class Editora:
    def __init__(self, nome):
        self.nome = nome
        self.obras = [Obra]

    def cadastroEditora(self):
        self.nome = input('Nome: ')

    def adicionarEditora(self, editora):
        self.obras.append(editora)

#----------------------------------------------------
#                       lIVRO

class Livro:
    def __init__(self, quantidadeTotal, quantidadeReservada) -> None:
        self.quantidadeTotal = int(quantidadeTotal)
        self.quantidadeReservada = int(quantidadeReservada)
        self.reservas = [Reserva]

#----------------------------------------------------
#                       OBRA

class Obra:
    def __init__(self, titulo, sinopise):
        self.titulo = titulo
        self.autor = Autor(nome=None, informacoes=None)
        self.editora = Editora(nome=None)
        self.sinopise = sinopise
        self.idioma = ...
        self.dataPublicacao = ...

    def adicionarTitulo(self):
        self.titulo = input('Titulo do Livro: ')

    def adicionarSinopse(self):
        self.sinopise = input('Sinopse: ')
    

#----------------------------------------------------
#                       RESERVA

class Reserva:
    def __init__(self, codigoReserva) -> None:
        self.codigoReserva = int(codigoReserva)
        self.livro = Livro
        self.portador = Usuario
        self.dataReserva = ...
        self.dataDevolucao = ...

#----------------------------------------------------
#                       USUARIO

class Usuario:
    def __init__(self, nome, email, senha, administrador) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha
        self.administrador = bool(administrador)

    def adicionarUsuario(self):
        self.nome = input('Digite o nome: ')
        self.email = input('Digite o email: ')
        self.senha = input('Digite o senha: ')
    
    def confirmacao_administrador(self):
        adm = input('Usuario Administrador: ')

        if adm == 'Sim':
            self.administrador = True
        elif adm == 'Nao':
            self.administrador = False
