import datetime as dt
import menu
import cadastra
import auxilio
import codigo
import ressources.cliente_resource as cliente_resource
import ressources.doacao_resource as doacao_resource
import ressources.carga_resource as carga_resource
import ressources.auxilio_resourse as auxilio_resource
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
    
    if escolha == 1: #referente a opção "gostaria de relatar um caso de meningite"
        print("=-"*10)
        print("por favor preencha as informações solicitadas: ")
        id = codigo.ids()
        cli = cadastra.cadastraCliente(data=dataHora,id=id) # chama a função cadastraV na pasta cadastraV 
        cliente_resource.create(cli) # adicionará os dados do cliente no banco de dados
        print("=-"*10)
        print("Agora preencha as informações do seu primeiro veiculo: ")
        idcliente = cliente_resource.find_one_by_codigo(id=id)
        idcliente=idcliente[0]
        
        veiculo = cadastra.cadastraV(id=idcliente,data=dataHora) #mostrará as informações, sobre o veiculo, a serem cadastradas pelo cliente
        veiculo_resource.create(veiculo) #usará as informações e as importará para nosso banco de dados
        print(cli)
        print("=-"*10)
        print("por favor anote o numero de seu  cadastro")
        print(id) # o id dado pelo programa é muito inportante para a ulização das funcionalidades do programa 
        print("obrigado por se cadastrar!!!")
        print("=-"*10)
        
        
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
        opcao = "altera"
        while opcao == "altera": #valor qualquer para entrar no looping while
            listadados =cliente_resource.find_all()
            print(listadados)
            id = str(input("seu codigo de cadastro: ")) 
            print("=-"*10)
            idcliente = cliente_resource.find_one_by_codigo(id=id)# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"
            if idcliente == None: # o cliente poderá decidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
                print('esse codigo não consta em nosso banco de dados')
                print('gostaria de tentar mais uma vez?')
                print('[1] Sim')
                print('[2] Não')
                opcao = int(input())        
            
                if opcao == 2:
                    input("aperte [enter] para ser enviado para o inicio")
                    opcao = "sair"# valor qualquer para sair do looping while
                elif opcao == 1:
                   opcao = "altera"
            else:
                 opcao = "alteraVeiculo" #valor qualquer para entrar no looping while
                 while opcao == "alteraVeiculo":
                       placa = str(input("por favor incira a placa do veiculo que gostaria de alterar: "))
                       veiculo = veiculo_resource.find_one_by_placa(str(placa))
                       if veiculo == None: # realizará uma busca pela placa, apenas se o numero da placa estiver na lista "listaPlacas"
                            print('essa placa não consta em nosso banco de dados')
                            print('gostaria de tentar mais uma vez?')
                            print('[1] Sim')
                            print('[2] Não')
                            opcao = int(input())
                            if opcao == 2:
                                input("aperte [enter] para ser enviado para o inicio")
                                opcao = "inicio"
                            elif opcao == 1:
                                 opcao = "alteraVeiculo"
                            
                       else:
                              
                            menu.seuVeiculo(veiculo=veiculo) 
                               
                            print("=-"*10)
                            veiculo = veiculo_resource.find_one_by_placa(placa=placa)
                            idveiculo = veiculo[0]
                            id = veiculo[1]
                            peso = veiculo[2]
                            comprimento = veiculo[3]
                            largura = veiculo[4]
                            altura = veiculo[5]
                            eixos = veiculo[6]
                            placa = veiculo[7]
                            marca = veiculo[8]
                            data = veiculo[9]

                            print(menu.seuVeiculo(veiculo)) #mostra o menu de informções para o cliente escolher qual deseja alterar
                            escolha = int(input("qual informação deseja alterar?"))
                            if escolha ==1:
                                    peso = float(input("qual o novo peso?"))
                            elif escolha ==2:
                                    comprimento = float(input("qual o novo comprimento?"))
                            elif escolha ==3:
                                        largura = float(input("qual a nova largura?"))
                            elif escolha ==4:
                                    altura = float(input("qual a nova altura?"))
                            elif escolha ==5:
                                    eixos = int(input("quantos eixos?"))
                            elif escolha ==6:
                                    placa = str(input("qual a nova placa?"))
                            elif escolha ==7:
                                    marca = str(input("qual a nova marca?"))
                            #montará um novo dicionario cujas informações iram popular a linha da tabela de nosso BD correspondente a placa do carro do cliente
                            vei = cadastra.seuVeiculo(idveiculo=idveiculo,id=id,peso=peso,comprimento=peso,largura=largura,altura=altura,eixos=eixos,placa=placa,marca=marca,data=data)
                            veiculo_resource.update(vei,placa)                                        
                            print(veiculo)
                            print("informação alterada com sucesso!!")
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
        print("Oque gostaria de deletar?")
        print("[1] Minha Conta")
        print("[2] um veiculo de minha conta")
        opcao = int(input())# o cliente poderá escolher se quer apagar a propria conta por completo ou apenas um um veiculo de sua conta
        if opcao == 1:
            opcao = 'deletar'
            while opcao == 'deletar':
                idCliente = str(input('Por favor informe seu codigo de cadastro: ')) 
                cliente=cliente_resource.find_one_by_codigo(id=idCliente)
                
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
                    chamada_resource.deletePorIdCliente(id=cliente[4])
                    veiculo_resource.deletePorId(id=cliente[4])
                    cliente_resource.delete(codigo=idCliente)
                    opcao = input ("seu cadastro foi apagado com sucesso")
                    print("aperte [enter] para ser enviado para o menu inicial")
                    opcao = "inicio"
                    print("=-"*10)
        elif opcao == 2:
             opcao = 'deletarCarro'
             while opcao == 'deletarCarro':
                   placa = str(input('Por favor o numero de sua placa do carro que deseja deletar de sua conta: '))
                   meuCarro = veiculo_resource.find_one_by_placa(placa=placa)
                   print(meuCarro)
                   if meuCarro == None: # o id é encontrado 
                      print("a placa de seu carro não foi encontrada em nosso banco de dados")
                      print("gostaria de tentar realizar essa operação novamente?")
                      print("[1] sim")
                      print("[2] não")
                      opcao = int(input())
                      if opcao == 1:
                         opcao = 'deletarCarro'
                      else:
                          opcao = "inicio"
                   else:
                        chamada_resource.deletePorIdVeiculo(id=meuCarro[0])
                        veiculo_resource.delete(placa=placa)
                        print("seu cadastro foi apagado com sucesso")
                        opcao = input ("aperte [enter] para ser enviado para o menu inicial")
                        opcao = "inicio"
                        print("=-"*10)
                        
       
    elif escolha == 6:
         print("Obrigado por utilizar nosso aplicativo")
    else:
        print("Escolha invalida!!")
    
    

    



