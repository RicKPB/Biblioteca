import re
from Class.classes import *


user = Usuario(nome=None, email= None, senha=None, administrador= None) 
obra = Obra(titulo=None, sinopise=None)
autor = Autor(nome=None, informacoes=None)
editora = Editora(nome=None)
reserva = Reserva(codigoReserva=0)
livro = Livro(titulo=None, autor=None, quantidadeLivros=None, quantidadeReservada=None)

autorTMP = Autor(nome=None, informacoes=None)
editoraTMP = Editora(nome=None)
livroTMP = Livro(titulo=None, autor=None, quantidadeLivros=None, quantidadeReservada=None)

lista_autores = []
lista_editoras = []
lista_obras = []
lista_reservas = []
lista_users = []


while True:
    selecao = input('[L]ogin | [R]egistrar | [F]inalizar: ').upper()

    if selecao == 'R':
        user.adicionarUsuario()
        user.confirmacao_administrador()
        lista_users.append(user)

    elif selecao == 'L':

        login = input('Login: ')
        senha = input('Senha: ')
    
    #   --------------------LOGIN ADMINISTRADOR--------------------------
        if login == user.nome and senha == user.senha:
            if user.administrador is True:
                while True:
                    print('Adiministrador Conectado\n')

                    print('Adicionar Obra')
                    print('Adicionar Autor')
                    print('Adionar Editora')
                    print('Adicionar Reserva')
                    print('Finalizar Reserva')
                    print('Consultar Acervo de Livros\n')

                    comando = input('Voce deseja realizar qual operacao: ')

    #   --------------------ADICIONAR OBRA----------------------      
                    if comando == 'Adicionar Obra':
                        
                        obra.adicionarTitulo()
                        obra.adicionarSinopse()
                        autorTMP.nome = input('Nome Autor: ')
                        editoraTMP.nome = input('Nome Editora: ')

                        for nome_autor in lista_autores:
                            if autorTMP.nome == nome_autor.nome:
                                obra.autor = autorTMP
                                print('Autor Adicionado')
                        
                        for nome_editora in lista_editoras:
                            if editoraTMP.nome == nome_editora.nome:
                                obra.editora = editoraTMP
                                print('Editora Adicionada')
                        

                        lista_obras.append(obra)
            
    #   --------------------ADICIONAR AUTOR----------------------      
                    elif comando == 'Adicionar Autor':
                        
                        autor.cadastroAutor()
                        autor.cadastroInformacoes()
                        lista_autores.append(autor)

                        if autor.nome == obra.autor.nome:
                            autor.adicionarObra(obra)


    #   --------------------ADICIONAR EDITORA----------------------                
                    elif comando == 'Adicionar Editora':
                        
                        editora.cadastroEditora()
                        lista_editoras.append(editora)

                        if editora.nome == obra.editora.nome:
                           editora.adicionarEditora(editora) 


    #   --------------------ADICIONAR LIVRO---------------------- 
                        elif comando == 'Adicionar Livro':
                            for nome_obra in lista_obras:
                                print(obra.titulo)

                            __ = input('Livro: ')
                            if __ == obra.titulo:
                                livro.adicionarQuantLivros()
                            print(f'{livro.quantidadeReservada}')
                      
    #   --------------------ADICIONAR RESERVA---------------------- 

                    elif comando == 'Adicionar Reserva':
                        
                        reserva.adiconarCodReserva()
                        print(reserva.codigoReserva)

                        livroTMP.titulo = input('Livro: ')

                        for nome_obra in lista_obras:
                            if livroTMP.titulo == obra.titulo:
                                reserva.adidcionarReserva(livro=livroTMP)
                                
                                

      
    #   --------------------FINALIZAR SISTEMA----------------------
                    sair = input('[S]air: ').upper().startswith('S')
                    if sair is True:
                        break
                    
    #   --------------------LOGIN USUARIO--------------------------
        elif login == user.nome and senha == user.senha:
            if user.administrador is not True:
                while True:
                    print('Usuario Conectado')

    #   --------------------FINALIZAR SISTEMA----------------------
                    sair = input('[S]air: ').upper().startswith('S')
                    if sair is True:
                        break
        
        else:
            print('Algo de errado aconteceu!')
            break
    
    elif selecao == 'F':
        print('Sistema Finalizado')
        break
