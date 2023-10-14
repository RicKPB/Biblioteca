#       ARQUIVO PARA A CRIACAO DE CLASSES PARA O SISTEMA






#----------------------------------------------------
#                       AUTOR

from mimetypes import init


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
#                       lIVRO

class Livro(Obra):
    def __init__(self, titulo, autor, quantidadeLivros, quantidadeReservada):
        super().__init__(titulo, autor)
        self.quantidadeLivros = quantidadeLivros
        self.quantidadeReservada = quantidadeReservada 
        self.reservas = list[Reserva] 

    def adicionarQuantLivros(self):
        self.quantidadeLivros = input('Quantidade de livros: ')
    
        
#----------------------------------------------------
#                       RESERVA

class Reserva:
    def __init__(self, codigoReserva) -> None:
        self.codigoReserva = int(codigoReserva)
        self.livro = Livro
        self.portador = Usuario
        self.dataReserva = ...
        self.dataDevolucao = ...


    def adiconarCodReserva(self):
        self.codigoReserva += 1
    

    def adidcionarReserva(self, livro):
        self.livro = livro


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
