import datetime as dt
import menu
import cadastra
import auxilio
import codigo
import ressources.cliente_resource as cliente_resource
import ressources.doacao_resource as doacao_resource
import ressources.carga_resource as carga_resource
import rankingAPI
import ressources.chamada_resource as chamada_resource
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
     
if opcao == 2:
     print("por favor preencha as seguintes informações")
     usuario = cadastra.cadastraCliente(data=hoje)
     cliente_resource.create(cliente=usuario)
     senha=usuario['senha']
     login=usuario['login']
     usuario = cliente_resource.find_one_by_SENHA(senha=senha,login=login)
     opcao = "inicio"
while escolha != 6 or opcao == "inicio":
    
    
    escolha = menu.menu() # chama a função menu criado na pasta menu.py
    
    if escolha == 1: #referente a opção "gostaria conferir os maiores doadores"
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
        print("=-"*10)
        idcliente = cliente_resource.find_one_by_codigo(id=id)# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"
        opcao = "alteraVeiculo" #valor qualquer para entrar no looping while
        menu.seuUsuario(usuario=usuario) 
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

        print(menu.seuUsuario(veiculo)) #mostra o menu de informções para o usuario escolher qual deseja alterar
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
        usu = cadastra.seuCadastro(id=usuario[0],nome=[1],cpf=[2],rg=[3],login=[4],senha=[5],nascimento=[6],sexo=[7],estadoCivil=[8],sangue=[9],data=[10])
        cliente_resource.update(cliente=usu,id=usuario[0])                                        
        print("informação alterada com sucesso!!")
        opcao = str(input("precione [enter] para retornar "))
        print("=-"*10)
        opcao = "inicio"
                 
    elif escolha == 4: #consulta referente a opção "gostaria de consultar meus dados" da função "menu" em "menu.py" 
        opcao = 'consulta'
        while opcao =='consulta':
              
              id = str(input("por favor digite seu codigo de usuario"))
              tuplacliente = cliente_resource.find_one_by_codigo(id=id)# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"
              if tuplacliente == None: # o cliente poderá decidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
                 print('esse codigo não consta em nosso banco de dados')
                 print('gostaria de tentar mais uma vez?')
                 print('[1] Sim')
                 print('[2] Não')
                 opcao = int(input())        
            
                 if opcao == 2:
                    input("aperte [enter] para ser enviado para o inicio")
                    opcao = "sair"# valor qualquer para sair do looping while
              
                 elif opcao == 1:
                    opcao = "consulta"
              else:
                   #colocará as informações a mostra do veiculo do cliente a mostra
                   print("suas informações de cadastro são:")
                   print('id:', tuplacliente[0])
                   print('nome:', tuplacliente[1])
                   print('cpf:', tuplacliente[2])
                   print('data de cadastro:', tuplacliente[3])
                   print('codigo de cliente:', tuplacliente[4])
                   print("=-"*10)
                   print("gostaria de ver as informações de um veiculo especifico?")
                   print("[1] sim")
                   print("[2] não")
                   opcao = int(input())
        if opcao == 1:
             opcao = 'consultaVeiculo'
             while opcao == 'consultaVeiculo':
                placa = str(input("for favor nos informe a placa desse veiculo: "))
                veiculo_consulta=veiculo_resource.find_one_by_placa(placa=placa)
                if veiculo_consulta == None:
                    print("-="*10)
                    print("veiculo não  encontrado gostaria de realizar essa consulta novamente? ")
                    print("[1] Sim")
                    print("[2] Não")
                    opcao = int(input())
                    if opcao == 2:
                         print("você será enviado para o menu inicial")
                         opcao='inicio'
                    elif opcao ==1:
                       opcao = 'consultaVeiculo'
                else:
                    #colocará as informações referente uma chamada especifica
                    print("suas informções de cadastro são:")
                    print('id_veiculo:', veiculo_consulta[0])
                    print('id_cliente:', veiculo_consulta[1])
                    print('peso:', veiculo_consulta[2])
                    print('comprimento:', veiculo_consulta[3])
                    print('largura:', veiculo_consulta[4])
                    print('altura:', veiculo_consulta[5])
                    print('eixos:', veiculo_consulta[6])
                    print('placa:', veiculo_consulta[7])
                    print('marca:', veiculo_consulta[8])
                    print('data de cadastro do veiculo:', veiculo_consulta[9])
                    
                    opcao = 2


        if opcao == 2:     
             opcao == "inicio"
             print("gostaria de ver o resumo de suas chamadas?" )
             print("[1] Sim")
             print("[2] Não")        
             opcao = int(input())
        if opcao == 2:
             input("aperte [enter] para ser enviado para o meu incial")
             opcao = 'inicio'
        elif opcao == 1:
             print("entrando no banco de dados de chamadas")
             opcao = "chamadas" # valor generico para entra no looping while
             while opcao == "chamadas": 
                    idChamada = str(input("por favor informe o codico da chamada que gostaria de verificar: "))
                    chamadasTupla = chamada_resource.find_one_by_codigo(chamada=idChamada)
                    
                    if chamadasTupla == None:
                         print("o id dessa chamada não foi encontrado") 
                         print("gostaria de tentar novamente? ")
                         print("[1] Sim")
                         print("[2] Não")
                         opcao = int(input())
                         if opcao == 1:
                              opcao = "chamadas"
                         elif opcao ==2:
                              opcao = str(input("precione [enter] para retornar ao inicio do programa"))
                              opcao = "inicio"
                         
                    else:
                         print("=-"*10)
                         auxilio.dbResumoChamada(chamadasTupla) 
                         print("-="*10)
                         opcao = str(input("aperte [enter] para ser enviado para o menu inicial"))
                         opcao = 'sair'       
                   
    
    elif escolha == 5: # apaga referente a opção "gostaria de deletar minhas informações" da função "menu" em menu.py
        print("Tem certeza de que gostaria de delertar sua conta?")
        print("[1] Sim, gostaria deletar minhas informações")
        print("[2] Não, gostaria de retornar ao inicio do programa")
        opcao = int(input())# o cliente poderá escolher se quer apagar a propria conta por completo ou apenas um um veiculo de sua conta
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
                        print("seu cadastro foi apagado com sucesso")
                        opcao = input ("aperte [enter] para ser enviado para o menu inicial")
                        opcao = "inicio"
                        print("=-"*10)
                    else:
                         print("por favor repita processo de deleção de cadastro conforme for pedido ")
                         opcao = 'deletar'
        
                        
       
    elif escolha == 6:
         print("Obrigado por utilizar nosso aplicativo")
    else:
        print("Escolha invalida!!")
    
    

    



