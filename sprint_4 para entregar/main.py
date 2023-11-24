import datetime as dt
import menu
import cadastra
import ressources.cliente_resource as cliente_resource
import ressources.doacao_resource as doacao_resource
import rankingAPI
escolha = 0
print("Seja bem vindo ao VitalSuport!!")
print("Para que posamos ajuda-lo por favor respoda conforme as altertivas indicadas")
opcao = 0
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')
menu.tenhoCadastro()
opcao = int(input())
if opcao == 1: # referente a opcao "sim, já tenho cadastro"
     print("por favor incira as informações a seguir:")
     usuario = None
     while usuario ==None:
        login = str(input("por favor incira seu login a seguir: "))
        senha = str(input("agora insira a senha de seu login: "))
        usuario = cliente_resource.find_one_by_SENHA(senha=senha, login=login)
        opcao = "inicio"
        if usuario == None:
             print("nome de usuario ou senha não encontrados")
             print("[1] gostaria de tentar repetir o processo?")
             print("[2] gostaria de realizar meu cadastro")
             print("[3] sair do aplicativo")
             opcao = int(input())
             if opcao == 1:
                  usuario=None
             elif opcao == 2:
                  usuario = 'sair'
             elif opcao == 3:
                  usuario = 'sair'
                  escolha = 6
     
if opcao == 2:# referente a opcao "ainda não possuo cadastro"
     print("por favor preencha as seguintes informações")
     usuario = cadastra.cadastraCliente(data=hoje) 
     cliente_resource.create(cliente=usuario)
     senha=usuario['senha']
     login=usuario['login']
     usuario = cliente_resource.find_one_by_SENHA(senha=senha,login=login) #as informações do usuario serão armazenadas em forma de tupla
     #e serão usadas para navegar pelas opções do aplicativo
     opcao = "inicio"
while escolha != 6 or opcao == "inicio":
    
    
    escolha = menu.menu() # chama a função menu criado na pasta menu.py
    
    if escolha == 1: #referente a opção "gostaria conferir o ranking dos maiores doadores"
        print("=-"*10)
        print("as maiores doações foram realizadas pelo usuario ")
        ranking=rankingAPI.ranking_ressources()
        for i in range(len(ranking)):
            for k, v in i.items():
                print(f'{k}:{v}')
            print("=-"*10)
        
        print("precione [enter] para retornar ao inicio")
        
        
        opcao = "inicio"
    elif escolha == 2: # gostaria de realizar uma doação"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        doacao =cadastra.cadastraDoacao(id=usuario[0],data=hoje,nome=usuario[1])
        print(doacao) # mostrará um lista de tuplas correspondete a tabela t_porto_cliente, essa informação
        doacao_resource.create(doacao=doacao)
        print('doacao realizada com sucesso')
        print('precione [ENTER]  para ser enviado para o inicio')
        print("=-"*10)
                
                
    elif escolha == 3: # referente a opção "gostaria de alterar uma informação"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        idUsuario = usuario[0]
        nome = usuario[1]
        cpf = usuario[2]
        rg = usuario[3]
        login = usuario[4]
        senha = usuario[5]
        nascimento = usuario[6]
        sexo = usuario[7]
        estadoCivil = usuario[8]
        sangue = usuario[9]
        data = usuario[10]
        usuario = usuario[11]

        print(menu.seuUsuario(usuario=usuario)) #mostra o menu de informções para o usuario escolher qual deseja alterar
        escolha = int(input("qual informação deseja alterar?"))
        if escolha ==1:
            nome = str(input("qual o novo nome?"))
        elif escolha ==2:
            login = str(input("qual o novo login?"))
        elif escolha ==3:
            senha = str(input("qual a nova senha?"))
        elif escolha ==4:
            estadoCivil = str(input("qual o novo estado civil?"))
        #montará um novo dicionario cujas informações iram popular a linha da tabela de nosso BD correspondente a ao id do usuario
        usu = cadastra.seuCadastro(id=idUsuario,nome=nome,cpf=cpf,rg=rg,login=login,senha=senha,nascimento=nascimento,sexo=sexo,estadoCivil=estadoCivil,sangue=sangue,data=data)
        cliente_resource.update(cliente=usu,id=usuario[0])                                        
        print("informação alterada com sucesso!!")
        opcao = str(input("precione [enter] para retornar "))
        print("=-"*10)
        opcao = "inicio"
                 
    elif escolha == 4: #consulta referente a opção "gostaria de consultar meus dados" da função "menu" em "menu.py" 
        opcao = 'consulta'
        usuario =  cliente_resource.find_one_by_id(id=usuario[0])
        print("aperte [enter] para ve as imformações de seu cadastro")
        opcao = str(input())
        print("suas informações de cadastro são:")
        print('id: ', usuario[0])
        print('login de usuario: ', usuario[4])
        print('nome do usuario: ', usuario[1])
        print('cpf: ', usuario[2])
        print('rg: ', usuario[3])
        print('nascimento: ', usuario[6])
        print('sexo: ', usuario[7])
        print('estado civil: ', usuario[8])
        print('tipo sanguineo: ', usuario[9])
        print('data da inscrição: ', usuario[10])
        print("=-"*10)
        print('precione [enter] para retornar ao menu inicial')
        opcao = str(input())
        opcao = "inicio"
            
                   
    
    elif escolha == 5: # apaga referente a opção "gostaria de deletar minhas informações" da função "menu" em menu.py
        print("Após a deleção de uma conta o esse program altomaticamente se enserrara")
        print("e o ex-usuario deverá reinicia-lo e cadastrar uma nova conta para poder utiliza-lo")
        print("Tem certeza de que gostaria de delertar sua conta?")
        print("[1] Sim, gostaria deletar minhas informações")
        print("[2] Não, gostaria de retornar ao inicio do programa")
        opcao = int(input())# o cliente poderá escolher se quer apagar a propria conta por completo ou retornar ao inicio
        if opcao == 1:
            opcao = 'deletar'
            while opcao == 'deletar':
                login = str(input('Por favor informe o login da conta que gostaria de deletar: '))                
                senha = str(input("agora insira a senha do login para poder excluir-lo"))
                cliente= cliente_resource.find_one_by_SENHA(senha=senha,login=login)
                if cliente == None:
                    print("seu codigo não foi encontrado gostaria de tentar de novo?")
                    print("[1] sim")
                    print("[2] não")
                    opcao = int(input())
                    if opcao == 1:
                        opcao = 'deletar'
                    else:
                         opcao = "inicio"
                else:
                    print("São esses, os dados da conta que gostaria de deletar?")
                    print("Nome: ",cliente[1])
                    print("CPF: ",cliente[2])
                    print("RG: ",cliente[3])
                    print("data de nascimento: ",cliente[6])
                    print("sexo biologico: ",cliente[7])
                    print("Estado civil: ",cliente[8])
                    print("grupo sanguineo: ",cliente[9])
                    print("[1] Sim")
                    print("[2] Não")
                    opcao = int(input())
                    if opcao == 1:
                        cliente_resource.delete(login=usuario[4],senha=usuario[5])
                        print("=-"*10)
                        print("seu cadastro foi apagado com sucesso")
                        print("lamentamos velo(a) partir")
                        print("=-"*10)
                        opcao = input ("aperte [enter] para ser enviado para encerrar o programa")
                        escolha = 6
                        print("=-"*10)
                    else:
                         print("por favor repita processo de deleção de cadastro conforme for pedido ")
                         opcao = 'deletar'
        
                        
       
    elif escolha == 6:
         print("=-"*10)
         print("Obrigado por utilizar nosso aplicativo")
    else:
        opcao = "inicio"
        print("Escolha invalida!!")
        print("=-"*10)
    
    

    



