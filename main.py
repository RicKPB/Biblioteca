from Class.classes import *


user = Usuario(nome=None, email= None, senha=None, administrador= None) 
obra = Obra(titulo=None, sinopise=None)
autor = Autor(nome=None, informacoes=None)
editora = Editora(nome=None)

while True:
    selecao = input('[L]ogin | [R]egistrar | [F]inalizar: ').upper()

    if selecao == 'R':
        user.adicionarUsuario()
        user.confirmacao_administrador()

    elif selecao == 'L':

        login = input('Login: ')
        senha = input('Senha: ')

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

                    if comando == 'Adicionar Obra':
                        
                        obra.adicionarTitulo()
                        obra.adicionarSinopse()


                    elif comando == 'Adicionar Autor':
                        
                        autor.cadastroAutor()
                        autor.cadastroInformacoes()
                    
                    elif comando == 'Adicionar Editora':
                        
                        editora.cadastroEditora()
                        

    #   --------------------FINALIZAR SISTEMA----------------------
                    sair = input('[S]air: ').upper().startswith('S')
                    if sair is True:
                        break
                    

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









#             # ------------------CADASTRO AUTOR----------------------
#             if comando == 'adicionar autor':
#                 autor_1 = Autor

#                 print('Informacoes Livro')

#                 autor_1.cadastroAutor(input('Nome Autor: '))
#                 autor_1.cadastroInformacoes(input('Informacoes Autor: '))
#                 continue
#             # --------------------------------------------------------

#             # ------------------CADASTRO EDITORA----------------------
#             if comando == 'adicionar editora':
#                 ediotra_1 = Editora

#                 editora_1.cadastroEditora('Nome Editar: ')
#                 continue
#             # --------------------------------------------------------

#             # ------------------CADASTRO LIVRO----------------------
#             if comando == 'adicionar livro':

#                 obra_1 = Obra

#                 obra_1.adicionarTitulo(input('Titulo: '))
#                 obra_1.adicionarSinopse(input('Sinopse: '))
#                 nomeTmp = input('Autor: ')

#                 if nomeTmp == autor_1.nome:
#                     obra_1.adicionarAutor(autor_1)

#                     print(obra_1.autor)

#                 else:
#                     print('Autor nao existe')

#         # --------------------FINALIZAR SISTEMA----------------------
#         sair = input('[S]air: ').upper().startswith('S')
#         if sair is True:
#             break
