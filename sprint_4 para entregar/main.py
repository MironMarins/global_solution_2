import datetime as dt
import menu
import cadastra
import auxilio
import codigo
import ressources.cliente_resource as cliente_resource
import ressources.veiculo_resource as veiculo_resource
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
     usuario = cliente_resource.create(cliente=usuario)
     opcao = "inicio"
while escolha != 6 or opcao == "inicio":
    
    
    escolha = menu.menu() # chama a função menu criado na pasta menu.py
    
    if escolha == 1: #referente a opção "gostaria de realizar meu cadatro"
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
    elif escolha == 2: # referente a opção "gostaria de cadastrar um veiculo a minha conta"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        opcao = "checar"
        while opcao == "checar":
            listadados =cliente_resource.find_all()
            print(listadados) # mostrará um lista de tuplas correspondete a tabela t_porto_cliente, essa informação
            #só tem a função de guiar a equipe de teste, ela será excluida na versão final
            id = input("seu codigo de cadastro: ")
                                            
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
                        opcao = "inicio"
                elif opcao == 1:
                        opcao = "checar"
            
            else: 
                 idcliente=idcliente[0]
                 veiculo = cadastra.cadastraV(id=idcliente,data=dataHora) # cliente poderá colocar as informações do novo veiculo que quiser adicionar
                 veiculo_resource.create(veiculo)#adicionará as informações do novo veiculo no banco de dados
                 print("veiculo adicionado com sucesso!")
                 print(veiculo_resource.find_one_by_placa(veiculo['placa']))
                 print("=-"*10)
                 opcao = "inicio"
            
                
                
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
                           
                      
                                           
                    
                    
    elif escolha == 5:
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        opcao = 0
        escolha = 'procura'
        id = str(input("seu ID de cadastro: "))
        while escolha == 'procura': # assim que o usuario colocar seu id corretamente
            
            tuplacliente=cliente_resource.find_one_by_codigo(id=id) 
            if tuplacliente == None: # o cliente poderá decidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
                print('esse codigo não consta em nosso banco de dados')
                print('gostaria de tentar mais uma vez?')
                print('[1] Sim')
                print('[2] Não')
                opcao = int(input())        
            
                if opcao == 2:
                    input("aperte [enter] para ser enviado para o inicio")
                    opcao = "inicio"# valor qualquer para sair do looping while
                    escolha="sair"
                elif opcao == 1:
                   id = str(input("seu ID de cadastro, novamente: "))
                   escolha = 'procura'
            else:
                idCliente=tuplacliente[0]
                nomeCliente=tuplacliente[1]
                cpfCliente=tuplacliente[2]
                dataCdastroCliente=tuplacliente[3]
                codigoCliente=tuplacliente[4]
                print("-="*10)
                print(tuplacliente)
                escolha = 'procuraV'
                placa = str(input("insira a placa de seu carro: "))
                while escolha == 'procuraV':
                     
                     tuplaveiculo=veiculo_resource.find_one_by_placa(placa=placa)
                     if tuplaveiculo == None:
                        print('essa placa não consta em nosso banco de dados')
                        print('gostaria de tentar mais uma vez?')
                        print('[1] Sim')
                        print('[2] Não')
                        opcao = int(input())        
            
                        if opcao == 2:
                           input("aperte [enter] para ser enviado para o inicio")
                           opcao = "inicio"# valor qualquer para sair do looping while
                           escolha ="sair"
                        elif opcao == 1:
                           escolha = 'procuraV'
                           placa = str(input("insira a placa de seu carro novamente: "))
                     else:
                          print("-="*10)
                          print(tuplaveiculo)
                          idVeiculo=tuplaveiculo[0]
                          idCliente=tuplaveiculo[1]
                          nrPeso=tuplaveiculo[2]
                          nrComprimento=tuplaveiculo[3]
                          nrLargura=tuplaveiculo[4]
                          nrAltura=tuplaveiculo[5]
                          nrEixos=tuplaveiculo[6]
                          cdPlaca=tuplaveiculo[7]
                          dsMarca=tuplaveiculo[8]
                          dtCadastro=tuplaveiculo[9]


                            
                          print("=-"*10)
                          print("nesse momento, seu veiculo esta comportando uma carga externa?") 
                          print("[1] Sim")
                          print("[2] Não")
                          escolha = 'sair'
                          opcao = int(input()) # o usuario deve informar se o veiculo esta comportando alguma carga externa (carreta)
                          cadastraCarga = "iniciar"
        if opcao == 1:
            print("por favor preencha a descrição da carga conforme e for solicitado")
            while cadastraCarga == "iniciar":
                
                print("=-"*10)
                codigoCarga = codigo.ids()
                dicCarga = cadastra.carga(placa=cdPlaca,data=dataHora,codigo=codigoCarga)
                print("=-"*10)
                print("verifique se as informações estão corretas: " )
                print(dicCarga)
                for k, v in dicCarga.items(): # o apresentado em forma de coluna, sendo as chaves são numeros de 1 a 6, menu de opções é automaticamente criado
                    print(f'{k}={v}')
                print("=-"*10)
                print("suas imformações estão corretas?")
                print("[1] Sim ")
                print("[2] Não ")
                opcao = int(input())
                if opcao == 2:
                   cadastraCarga = "iniciar"   
                   print("por favor insira as informações de sua carga novamente")
                elif opcao == 1:
                     carga_resource.create(dicCarga)
                     cadastraCarga = "sair"
                     print("=-"*10)

                     tuplacarga = carga_resource.find_one_by_codigo(codigo=codigoCarga)
                     cdCargaPlaca = tuplacarga[0]
                     nrPesoCarga = tuplacarga[1]
                     nrComprimentoCarga = tuplacarga[2]
                     nrAlturaCarga = tuplacarga[3]
                     nrLarguraCarga = tuplacarga[4]
                     nrEixosCarga = tuplacarga[5]
                     dsTipoCarga = tuplacarga[6]
                     dtCadastroCarga = tuplacarga[7]
                     idCarga = tuplacarga[8]
                     cdCarga = tuplacarga[9]

           
            veiculoTotal = auxilio.veiculoTotal(pesoV=nrPeso,
                                                pesoC=nrPesoCarga,
                                                comprimentoV=nrComprimento,
                                                comprimentoC=nrComprimentoCarga,
                                                alturaV=nrAltura,
                                                alturaC=nrAlturaCarga,
                                                larguraV=nrLargura,
                                                larguraC=nrAlturaCarga)
            opcao = 'passaV'
             # pesoV e comprimentoC serão somados com o pesoV e comprimentoV e devolvidos como pesoTotal e comprimentoTotal
                            # a maior altura e largura dentre veiculo e carga serão a alturaTotal e larguraTotal
            print("vt1",veiculoTotal)
        elif opcao == 2:# Caso o veiculo não tenha carga externa o pesoC, alturaC, comprimentoC e larguraC serão todos iguais a 0
                veiculoTotal = auxilio.veiculoTotal(pesoV=nrPeso,
                                                    pesoC=0,
                                                    comprimentoV=nrComprimento,
                                                    comprimentoC=0,
                                                    alturaV=nrAltura,
                                                    alturaC=0,
                                                    larguraV=nrLargura,
                                                    larguraC=0)
                idCarga=None
                opcao = 'passaV'
                print("vt2",veiculoTotal) # os atributos de veiculoTotal serão guadados em pesoTotal, ComprimentoTotal, larguraTotal e alturatotal
        if opcao == 'passaV':
            pesoTotal = veiculoTotal['pesoTotal']
            print(pesoTotal)
            comprimentoTotal = veiculoTotal['comprimentoTotal']
            print(comprimentoTotal)
            alturaTotal = veiculoTotal['alturaTotal']
            print(alturaTotal)
            larguraTotal = veiculoTotal['larguraTotal']
            print(larguraTotal)
            dic_auxilio = auxilio.auxilio() # o dicionario "auxilio" será chamado da função "auxilio"  em auxilio.py e quardado em dic_auxilio 
            dic_modal = dic_auxilio['modal'] # o dicionario da chave modal no dicionario dic_auxilio será quardado em dic_modal
            modalT = auxilio.escolhaModal(pesoTotal=pesoTotal,dic_modal=dic_modal) # o valor de pesoTotal será usado para escolher o modal correto no dicionario dic_modal
            if modalT == 'Modal leve':
                tuplaAuxilio = auxilio_resource.find_all_auxilio()
                modalT = tuplaAuxilio[2]
            
            elif modalT == 'Modal medio':
                tuplaAuxilio = auxilio_resource.find_all_auxilio()
                modalT = tuplaAuxilio[3]
            elif modalT == 'Modal pesado':  
                tuplaAuxilio = auxilio_resource.find_all_auxilio() 
                modalT = tuplaAuxilio[4]  
         
            print(modalT)
        
            print("=-"*10)
            print("por favor digite o numero correspondente ao seu problema")
            problemas = auxilio_resource.find_all_problemas() # a tupla referente a a tabela do banco dados "T_PORTO_PROBLEMA"
            for i in range(len(problemas)): # o apresentado em forma de coluna, sendo as chaves são numeros de 1 a 6, menu de opções é automaticamente criado
                print("[" + str(problemas[i][0]) + "] " + str(problemas[i][1]))
        
        
            opcao = int(input())
            problema = opcao
            print(problema)
        
            print("=-"*10)
                        
            especificacao = auxilio.expecificacao() # o dicionario de expecificações será chamado da função "expecificacao" em auxilio.py 
        
        if opcao == 1: # referente a opção ' O veiculo simplesmente parou no meio da estrada e não anda mais', do dicionario "problema"
                gasolina_dic = especificacao[str(opcao)]
                for k, v in gasolina_dic.items():
                    print(f'{k}={v}')
                opcao = int(input()) # o usuario deve escolher uma opção referente ao dicionario guardado na chave do dicionario especificacao
                
                
                especificacao = gasolina_dic[str(opcao)]
                print(especificacao)
                
                if opcao == 1: #referente a opção ' há gasolina no tanque' do dicionaro "gasolina" na funcao especificacao
                    dbEspecificacao = 1
                    solucao = modalT[0] #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                    print("entamos enviando um modal", modalT[1], "para a sua localização" )
                    opcao='chamada'                    
                    
                elif opcao == 2: #referente a opção ' o tanque esta vazio' do dicionaro "gasolina" na funcao especificacao
                    dbEspecificacao = 2
                    moto = dic_auxilio['moto']
                    solucao = moto #quarda valor moto em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                    
                    print("estamos enviando um", moto, "com gasolina para a sua localização")
                    solucao=1
                    opcao='chamada'
        elif opcao == 2: # referente a opção ' O veiculo estava estacionado e não quer ligar', do dicionario "problema"
                eletrico = especificacao['2'] 
                print("o painel esta ascendendo?")
                for k, v in eletrico.items():
                    print(f'{k}={v}')
                opcao = int(input()) # o usuario deve escolher uma opção referente ao dicionario guardado na chave do dicionario especificacao   
                especificacao = eletrico[str(opcao)]
                print(especificacao)    
                if opcao == 1: #referente a opção ' O painel esta ligando' do dicionaro "esletrico" na funcao especificacao
                    dbEspecificacao = 3
                    solucao = modalT[0] #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                    print("entamos enviando um modal", modalT[1], "para a sua localização" )
                    opcao='chamada'
                elif opcao == 2: #referente a opção ' O painel não liga' do dicionaro "esletrico" na funcao especificacao
                    
                     moto = dic_auxilio['moto']
                     dbEspecificacao = 4
                     solucao = moto #quarda valor moto em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                     print("estamos enviando um", moto, "com material carregar sua bateria, para a sua localização")
                     solucao =1
                     opcao='chamada'
        elif opcao == 3:# referente a opção ' Meu pneu furou/extourou, não tenho step/macaco', do dicionario "problema"
                pneu = especificacao['3']
                especificacao = pneu
                
                tecnico = dic_auxilio['tecnico']
                solucao = tecnico #quarda valor tecnico em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("estamos enviando um", tecnico, "com step para a sua localização")
                dbEspecificacao = None
                solucao=2
                opcao='chamada'
        elif opcao == 4:# referente a opção ' Ouvi um barulho e agora meu veiculo esta se comportando de maneira estranha', do dicionario "problema"
                print("Consegue identificar de onde esta vindo o barulho? ")
                barulho = especificacao['4']
                for k, v in barulho.items():
                    print(f'{k}={v}')
                opcao = int(input()) # como barulho estranho é um problema de dificio averiguação colocamos modal como unica opção de solução
                if opcao == 1:
                     dbEspecificacao = 7
                elif opcao ==2:
                     dbEspecificacao = 8
                elif opcao ==3:
                     dbEspecificacao = 9
                elif opcao ==4:
                     dbEspecificacao = 10
                elif opcao ==5:
                     dbEspecificacao = 11
                elif opcao ==6:
                     dbEspecificacao = 12
                
                especificacao = barulho[str(opcao)]
                solucao = modalT[0] #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("entamos enviando um modal", modalT[1], "para a sua localização" )
                opcao='chamada'
        elif opcao == 5:# referente a opção ' Um cheiro estranho', do dicionario "problema"
                print("que tipo de cheiro esta sentindo?")
                cheiro = especificacao['5']
                for k, v in cheiro.items():
                    print(f'{k}={v}')
                opcao = int(input()) # # como cheiro de queimado ou gasolina podem estar ambos ligados a um problem serio colocamos modal como unica opção de solução   
                especificacao = cheiro[str(opcao)]
                print(especificacao)
                if opcao == 1:
                     dbEspecificacao = 5
                     opcao='chamada'
                elif opcao ==2:
                     dbEspecificacao = 6
                solucao = modalT[0] #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("por precausão, é melhor estacionar o carro")
                print("entamos enviando um ", modalT[1], "para a sua localização" )
                
                opcao='chamada'
        elif opcao == 6:# referente a opção ' Vejo fumaça saindo do meu veiculo', do dicionario "problema"
                fumaça = especificacao['6']
                especificacao = fumaça 
                solucao = modalT[0] #quarda valor modal em solucao para ser adicionado no dicionario da função "resumoChamadas" em auxilio.py
                print("por precausão, é melhor estacionar o carro") #como a visão de fumaça pode ser um problema seriu no veiculo colocamos o modal como 
                                                                    #solução para esse caso
                print("entamos enviando um modal", modalT[1], "para a sua localização" )
                dbEspecificacao = None
                opcao='chamada'
        if opcao == 'chamada':
            codigoChamada =codigo.ids()
            chamada = auxilio.resumoChamada(idProblema=problema, idAuxilio=solucao,
                                        idCliente=idCliente, idCarga=idCarga,
                                        idEspecificacao=dbEspecificacao,
                                        idVeiculo=idVeiculo, data=dataHora, idCodigo=codigoChamada)
            print(chamada)
            chamada_resource.create(chamada=chamada)
            print("=-"*10) #todsas os valores pertinentes a chamada serão adicionados a função resomuChamad em aucilio.py e serão guardadas no valor variavel resumoChamada
            print('por favor anote o id dessa chamada')
            print("seu codigo é:" + str(codigoChamada)) # mostrará o id da chamada para o usuario
            print("=-"*10)
            print("gostaria de ver o resumo de sua chamada?")
            print("[1] Sim")
            print("[2] Não")
            opcao = int(input())
            if opcao == 1: # mostra dicionario do resumo da chamada em forma de colunas
                tuplaChamada =chamada_resource.find_one_by_codigo(chamada=codigoChamada)
            
                auxilio.dbResumoChamada(tuplaChamada)
            
                    

                input("aperte [Enter] para ser eviado para o inicio")
                print("-="*10)
                opcao = "inicio"       
            elif opcao == 2:# leva o usuario para o inicio do programa
                input("aperte enter para ser enviado para o inicio")          
                opcao ="inicio"
    elif escolha == 6: # apaga referente a opção "gostaria de deletar minhas informações" da função "menu" em menu.py
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
                        
       
    elif escolha == 7:
         print("Obrigado por utilizar nosso aplicativo")
    else:
        print("Escolha invalida!!")
    
    

    



