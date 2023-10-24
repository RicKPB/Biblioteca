#       ARQUIVO PARA A CRIACAO DE CLASSES PARA O SISTEMA
from dataclasses import dataclass
from datetime import datetime
from tarfile import data_filter

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

    def consultarAutor(self):
        return(f'Nome: {self.nome}\n'
            f'Informacoes: {self.informacoes}')


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

    def consultarEditora(self):

        return (f'Editora: {self.nome}')


#----------------------------------------------------
#                       OBRA

class Obra:
    def __init__(self, titulo, sinopise, data_publicacao):
        self.titulo = titulo
        self.autor = Autor(nome=None, informacoes=None)
        self.editora = Editora(nome=None)
        self.sinopise = sinopise
        self.idioma = ...
        self.dataPublicacao = data_publicacao

    def adicionarTitulo(self):
        self.titulo = input('Titulo do Livro: ')

    def adicionarSinopse(self):
        self.sinopise = input('Sinopse: ')

    def adicionarData(self, data_publicacao):
        data_publicacao = input('Data YYYY-MM-DD: ')

        try:
            self.dataPublicacao = datetime.strptime(data_publicacao, '%Y-%m-%d')
        except ValueError:
            print('Formato de data invalido. Use YYYY-MM-DD.')
            self.dataPublicacao = None

    
    def consultaObra(self):

        return (f'Titulo: {self.titulo}\n'
            f'Autor: {self.autor.nome}\n'
            f'Editora: {self.editora.nome}\n'
            f'Sinopise: {self.sinopise}\n'
            f'Data Publicado: {self.dataPublicacao}')


#----------------------------------------------------
#                       lIVRO

class Livro(Obra):
    def __init__(self, titulo, autor, data_publicacao):
        super().__init__(titulo, autor, data_publicacao)
        self.quantidadeLivros = 0
        self.quantidadeReservada = 0 
        self.reservas = list[Reserva] 

    def adicionarQuantLivros(self):
        self.quantidadeLivros = input('Quantidade de livros: ')

    def consultarLivro(self):

        livroTMP = input('Qaul livro deseja consultar: ')

        if livroTMP in self.titulo:
            return (f'Titulo: {self.titulo}\n'
                    f'Quantidade De Livros: {self.quantidadeLivros}\n'
                    f'Quantidade Resevada: {self.quantidadeReservada}')
    
#----------------------------------------------------
#                       RESERVA

class Reserva:
    def __init__(self, codigoReserva, data_Res, dataTMP) -> None:
        self.codigoReserva = int(codigoReserva)
        self.livro = Livro
        self.portador = Usuario
        self.dataReserva = data_Res
        self.dataDevolucao = dataTMP


    def adiconarCodReserva(self):
        self.codigoReserva += 1
    

    def adidcionarReserva(self, livro):
        self.livro = livro

    def adidcionarPortador(self, user):
        self.portador = user
    
    def dataReservaRealizada(self):
        self.dataReserva = datetime.now()
    
    def dataDaDevolucao(self, dataTMP):
        dataTMP = input('Data Devolucao: YYYY-MM-DD')

        try:
            self.dataDevolucao = datetime.strptime(dataTMP, '%Y-%m-%d')
        except ValueError:
            print('Formato de data invalido. Use YYYY-MM-DD.')
            self.dataDevolucao = None


    def consultarReservas(self):

        return (f'Serial: {self.codigoReserva}\n'
                f'Livro: {self.livro}\n'
                f'Portador: {self.portador}\n'
                f'Data Reserva: {self.dataReserva}\n'
                f'Data Devolucao: {self.dataDevolucao}')


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
        else:
            self.administrador = False

    
