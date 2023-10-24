import os 
from Class.classes import *


user = Usuario(nome=None, email= None, senha=None, administrador= None) 
obra = Obra(titulo=None, sinopise=None, data_publicacao=None)
autor = Autor(nome=None, informacoes=None)
editora = Editora(nome=None)
reserva = Reserva(codigoReserva=0, data_Res=None, dataTMP=None)
livro = Livro(titulo=None, autor=None, data_publicacao=None)

autorTMP = Autor(nome=None, informacoes=None)
editoraTMP = Editora(nome=None)
livroTMP = Livro(titulo=None, autor=None, data_publicacao=None)
userTMP = Usuario(nome=None, email= None, senha=None, administrador= None)

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
        for usuario in lista_users:
            print(usuario)
            
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

                            os.system('cls')
                            
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

                            obra.adicionarData(data_publicacao=None)
                            

                            lista_obras.append(obra)
            
                        #--------------------ADICIONAR AUTOR----------------------      
                        elif comando == 'A':
                            
                            os.system('cls')
                            
                            autor.cadastroAutor()
                            autor.cadastroInformacoes()
                            lista_autores.append(autor)

                            if autor.nome == obra.autor.nome:
                                autor.adicionarObra(obra)

                        #--------------------ADICIONAR EDITORA----------------------                
                        elif comando == 'E':
                            
                            os.system('cls')
                            
                            editora.cadastroEditora()
                            lista_editoras.append(editora)

                            if editora.nome == obra.editora.nome:
                                editora.adicionarEditora(obra) 


                        #--------------------ADICIONAR LIVRO---------------------- 
                        elif comando == 'L':
                            
                            os.system('cls')
                            
                            for nome_obra in lista_obras:
                                print(obra.titulo)

                            __ = input('Livro: ')
                            if __ == obra.titulo:
                                livro.adicionarQuantLivros()
                               
                        #--------------------ADICIONAR RESERVA---------------------- 
                        elif comando == 'R':
                            
                            os.system('cls')
                            
                            reserva.adiconarCodReserva()
                            print(reserva.codigoReserva)

                            userTMP.nome = input('Digite o usuario: ')
                            for nome_user in lista_users:
                                if userTMP.nome == nome_user:
                                    reserva.adidcionarPortador(user=userTMP)

                            livroTMP.titulo = input('Livro: ')
                            for nome_obra in lista_obras:
                                if livroTMP.titulo == obra.titulo:
                                    reserva.adidcionarReserva(livro=livroTMP)

                            
                            reserva.dataReservaRealizada()
                            reserva.dataDaDevolucao(dataTMP=None)
                            
                            livro.quantidadeReservada += 1
                                
                    elif comando == 'C':

                        print('[O]bra | [A]utor | [E]ditora | [R]eserva | [L]ivro')

                        comando = input('Qual Operacao: ').upper()

                        if comando == 'O':
                            
                            os.system('cls')
                            
                            print(obra.consultaObra())

                        if comando == 'A':
                            os.system('cls')
                            
                            print(autor.consultarAutor())
                            if obra.autor.nome == autor.nome:
                                print(obra.titulo)
                            
                        if comando == 'E':
                            os.system('cls')
                            
                            print(editora.consultarEditora())
                            if obra.editora.nome == editora.nome:
                                print(obra.titulo)

                        if comando == 'R':
                            os.system('cls')
                            
                            print(reserva.consultarReservas())

                        if comando == 'L':
                            os.system('cls')
                           
                            print(livro.consultarLivro())
                            for reservaTMP in lista_reservas:
                                print(reservaTMP)

                    #   --------------------FINALIZAR SISTEMA----------------------
                    sair = input('[S]air: ').upper().startswith('S')
                    if sair is True:
                        break
                    
    #   --------------------LOGIN USUARIO--------------------------
        if login == user.nome and senha == user.senha:
            if user.administrador is False:
                while True:
                    print('Usuario Conectado')

                    comando = input('Consultar [L]ivros || Minhas [R]eservas: ').upper()

                    if comando == 'L':
                        print(lista_obras)

                    if comando == 'R':
                        
                        if reserva.portador == user.nome:
                            print(reserva)

    #   --------------------FINALIZAR SISTEMA----------------------
                    sair = input('[S]air: ').upper().startswith('S')
                    if sair is True:
                        break
        else:
            os.system('cls')

            print('Login Incorreto')

    elif selecao == 'F':
        print('Sistema Finalizado')
        break
