

class Obra:
    def __init__(self, titulo, sinopise, editora, autor):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.sinopise = sinopise
        self.idioma = ...
        self.dataPublicacao = ...

    def adicionarTitulo(self, titulo):
        self.titulo = titulo

    def adicionarSinopse(self, sinopse):
        self.sinopise = sinopse

    def adicionarAutor(self, autor):
        self.autor = autor
        
