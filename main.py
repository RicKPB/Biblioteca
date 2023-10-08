

user = None
autor_1 = None
ediotra_1 = None

while True:


    selecao = input('[L]ogin | [R]egistrar: ').upper()

    #--------------------CRIAR LOGIN------------------------
    if selecao == 'L':
       
        nomeTmp = input('Nome: ')
        emailTmp = input('E-mail: ')
        senhaTmp = input('Senh: ')
        administradorTmp = input('[T]rue | [F]alse: ').upper()
        if administrador == 'T':
            administrador = True
        else:
            administrador = False
        
        user = Usuario(nomeTmp, emailTmp, senhaTmp, administradorTmp)  
    #--------------------------------------------------------
    
    #--------------------REALIZAR LOGIN----------------------
    elif selecao == 'R':
        
        login = input('Login: ')
        senha = input('Senha: ')

        if login != user.nome:
            print('Nome Incorreto')
            continue
            
        if senha != user.senha:
            print('senha errada')
            continue
        #--------------------------------------------------------
        
        #--------------------SISTEMA EM FUNCIONAMENTO----------------------
        if user.administrador is True:
            print('Adicionar Livro\n')
            print('Adicionar Autor\n')
            print('Adionar Editora\n')
            print('Adicionar Reserva\n')
            print('Finalizar Reserva\n')
            print('Consultar Acervo de Livros')

            comando = input('Voce deseja realizar qual operacao: ')

            # ------------------CADASTRO AUTOR----------------------
            if comando == 'adicionar autor':
                
                autor_1 = Autor()

                print('Informacoes Livro')

                autor_1.cadastroAutor(input('Nome Autor: '))
                autor_1.cadastroInformacoes(input('Informacoes Autor: '))
                continue
            #--------------------------------------------------------

            # ------------------CADASTRO EDITORA----------------------
            if comando == 'adicionar editora':

                ediotra_1 = Editora()

                ediotra_1.cadastroEditora('Nome Editar: ')
                continue
            #--------------------------------------------------------

            # ------------------CADASTRO LIVRO----------------------
            if comando == 'adicionar livro':

                obra_1 = Obra()

                obra_1.adicionarTitulo(input('Titulo: '))
                obra_1.adicionarSinopse(input('Sinopse: '))
                nomeTmp = input('Autor: ')

                if nomeTmp == autor_1.nome:
                    obra_1.adicionarAutor(autor_1)
                
                    print(obra_1.autor)

                else:
                    print('Autor nao existe')


        #--------------------FINALIZAR SISTEMA----------------------
        sair = input('[S]air: ').upper().startswith('S')
        if sair is True:
            break

    

        
        