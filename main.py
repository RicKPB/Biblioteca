import os
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

                    print('[A]dicionar  |   [C]onsultar')

                    comando = input('Voce deseja realizar qual operacao: ').upper()
                    if comando == 'A':
                        print('[O]bra | [A]utor | [E]ditora | [R]eserva | [L]ivro')

                        comando = input('Qual Operacao: ').upper()
                        #--------------------ADICIONAR OBRA----------------------      
                        if comando == 'O':
                        
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
            
                        #--------------------ADICIONAR AUTOR----------------------      
                        elif comando == 'A':
                            
                            autor.cadastroAutor()
                            autor.cadastroInformacoes()
                            lista_autores.append(autor)

                            if autor.nome == obra.autor.nome:
                                autor.adicionarObra(obra)

                        #--------------------ADICIONAR EDITORA----------------------                
                        elif comando == 'E':
                            
                            editora.cadastroEditora()
                            lista_editoras.append(editora)

                            if editora.nome == obra.editora.nome:
                                editora.adicionarEditora(editora) 


                        #--------------------ADICIONAR LIVRO---------------------- 
                        elif comando == 'L':
                            for nome_obra in lista_obras:
                                print(obra.titulo)

                            __ = input('Livro: ')
                            if __ == obra.titulo:
                                livro.adicionarQuantLivros()
                               
                        #--------------------ADICIONAR RESERVA---------------------- 
                        elif comando == 'R':
                            
                            reserva.adiconarCodReserva()
                            print(reserva.codigoReserva)

                            livroTMP.titulo = input('Livro: ')

                            for nome_obra in lista_obras:
                                if livroTMP.titulo == obra.titulo:
                                    reserva.adidcionarReserva(livro=livroTMP)
                                
                    elif comando == 'C':

                        print('[O]bra | [A]utor | [E]ditora | [R]eserva | [L]ivro')

                        comando = input('Qual Operacao: ').upper()

                        if comando == 'O':
                            os.system('cls')
                            for obra.titulo in lista_obras:
                                print(obra.titulo)

                        if comando == 'A':
                            pass

                        if comando == 'E':
                            pass

                        if comando == 'R':
                            pass

                        if comando == 'L':
                            pass 
                    #   --------------------FINALIZAR SISTEMA----------------------
                    sair = input('[S]air: ').upper().startswith('S')
                    if sair is True:
                        break
                    
    #   --------------------LOGIN USUARIO--------------------------
        elif login == user.nome and senha == user.senha:
            if user.administrador is not True:
                while True:
                    print('Usuario Conectado')

                    __ = input('Consultar Livros [S]im: ').upper()

                    if __ == 'S':
                        print(lista_obras)


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
