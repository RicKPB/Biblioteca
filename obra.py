from autor import Autor
from editora import Editora

class Obra():
    def __init__(self, titulo, sinopise):
        self.titulo = titulo
        self.editora = Editora()
        self.autor = Autor()
        self.sinopise = sinopise
        self.idioma = ...
        self.dataPublicacao = ...

    def adicionarTitulo(self, titulo):
        self.titulo = titulo

    def adicionarSinopse(self, sinopse):
        self.sinopise = sinopse

    def adicionarAutor(self, autor):
        self.autor = autor
        
