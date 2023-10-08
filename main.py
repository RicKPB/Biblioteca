from usuario import Usuario

user = None

while True:

    selecao = input('[L]ogin | [R]egistrar: ').upper()

    if selecao == 'L':
       
        nome = input('Nome: ')
        email = input('E-mail: ')
        senha = input('Senh: ')
        administrador = input('[T]rue | [F]alse: ').upper()
        if administrador == 'T':
            administrador = True
        else:
            administrador = False
        
        user = Usuario(nome, email, senha, administrador)
    
    elif selecao == 'R':
        
        login = input('Login: ')
        senha = input('Senha: ')

        if login != user.nome:
            print('Nome Incorreto')
            continue
            
        if senha != user.senha:
            print('senha errada')
            continue

        sair = input('[S]air: ').upper().startswith('S')
        if sair is True:
            break

    

        
        