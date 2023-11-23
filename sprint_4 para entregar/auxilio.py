import codigo
import ressources.cliente_resource as cliente_resource
import ressources.veiculo_resource as veiculo_resource
import ressources.carga_resource as carga_resource
import ressources.auxilio_resourse as auxilio_resource
import ressources.chamada_resource as chamada_resource

def auxilio():
        ajuda = {}
        reboque = {}
        
        reboque['modal1'] = 'Modal leve'
        reboque['modal2'] = 'Modal medio'
        reboque['modal3'] = 'Modal pesado'

        ajuda['moto'] = 'motoboy'
        ajuda['tecnico'] = 'mecanico'
        ajuda['modal'] = reboque
        return ajuda




def problema():
        problema ={}

        problema['1'] = ' O veiculo simplesmente parou no meio da estrada e não anda mais'
        problema['2'] = ' O veiculo estava estacionado e não quer ligar'
        problema['3'] = ' Meu pneu furou/extourou, não tenho step/macaco'
        problema['4'] = ' Ouvi um barulho e agora meu veiculo esta se comportando de maneira estranha'
        problema['5'] = ' Um cheiro estranho'
        problema['6'] = ' Vejo fumaça saindo do meu veiculo'
        return problema

def expecificacao():
        expecificacao = {}
        gasolina = {}
        eletrico = {}
        cheiro = {}
        barulho = {}
        

        gasolina['1'] = ' há gasolina no tanque'
        gasolina['2'] = ' o tanque esta vazio'

        eletrico['1'] = ' O painel esta ligando'
        eletrico['2'] = ' O painel não liga'

        cheiro['1'] = ' cheiro de queimado'
        cheiro['2'] = ' cheiro de gasolina'
               
        barulho['1'] = ' barulho vindo da frente do veiculo'
        barulho['2'] = ' barulho vindo de traz do veiculo'
        barulho['3'] = ' barulho vindo do lado direito'
        barulho['4'] = ' barulho vindo do lado esquerdo'
        barulho['5'] = ' barulho vindo de embaixo do veiculo'
        barulho['6'] = ' barulho vindo de dentro do veiculo'
        
        expecificacao['1'] = gasolina
        expecificacao['2'] = eletrico
        expecificacao['3'] = ' pneu furado'
        expecificacao['4'] = barulho
        expecificacao['5'] = cheiro
        expecificacao['6'] = ' fumaça saindo do meu veiculo'

        return expecificacao

def veiculoTotal(pesoV,pesoC,comprimentoV,comprimentoC,alturaV,alturaC,larguraV,larguraC):
        veiculoTotal = {}
        
        pesoTotal = pesoV + pesoC
        comprimentoTotal = comprimentoC + comprimentoV

        if alturaC < alturaV:
            alturaTotal = alturaV
        else:
            alturaTotal = alturaC
        if larguraC < larguraV:
            larguraTotal = larguraV
        else:
            larguraTotal = larguraC
        veiculoTotal['pesoTotal'] = pesoTotal
        veiculoTotal['comprimentoTotal'] = comprimentoTotal
        veiculoTotal['alturaTotal'] = alturaTotal
        veiculoTotal['larguraTotal'] = larguraTotal

        return veiculoTotal
def escolhaModal(pesoTotal,dic_modal):
    
    
    if pesoTotal < 5.0:
          modalT = dic_modal['modal1'] 
    elif pesoTotal >= 5.0 and pesoTotal <15.0:
          modalT = dic_modal['modal2']
    else:
         modalT = dic_modal['modal3']
    return modalT
          
                
def resumoChamada(idProblema,idCliente,idAuxilio,idVeiculo,idEspecificacao,idCarga,data,idCodigo):
    resumoChamada = {}
        
    resumoChamada['idProblema'] = idProblema
    resumoChamada['idCliente'] = idCliente
    resumoChamada['idAuxilio'] = idAuxilio
    resumoChamada['idVeiculo'] = idVeiculo
    resumoChamada['idEspecificacao'] = idEspecificacao
    resumoChamada['idCarga'] = idCarga
    resumoChamada['dtChamada'] = data
    resumoChamada['idCodigo'] = idCodigo   
    return resumoChamada 

def dbResumoChamada(tuplaChamada):
                print(tuplaChamada)
                idchamada = tuplaChamada[0]
                print("o id dessa chamada", idchamada)
                dtChamada = tuplaChamada[7]
                print("=-"*10)
                print("Na data de ", dtChamada)
                clienteTupla = cliente_resource.find_one_by_id(tuplaChamada[2])
                print("O cliente " + str(clienteTupla[1]))
                print("portador do cpf "+ str(clienteTupla[2]))
                veiculoTupla = veiculo_resource.find_one_by_idVeiculo(tuplaChamada[4])
                auxilioTupla = auxilio_resource.find_one_by_id_auxilio(tuplaChamada[3])
                print("solicitou um " + str(auxilioTupla[1]))
                print("para seu veiculo "+ str(veiculoTupla[8]) + " de placa "+ str(veiculoTupla[7]))
                print("com " + str(veiculoTupla[2]) + " toneladas, " + str(veiculoTupla[3]) +" de comprimento" )
                print(str(veiculoTupla[5]) + " de altura e " + str(veiculoTupla[4]) +" de largura" )
                idCarga = carga_resource.find_one_by_id(tuplaChamada[6])
                if idCarga ==None:
                      print("não portando carga")
                else:
                      print("portando uma carga do tipo" + str(idCarga[6]))
                      print("com " + str(idCarga[1]) + " toneladas, " + str(idCarga[2]) +" de comprimento" )
                      print(str(idCarga[3]) + " de altura e " + str(idCarga[4]) +" de largura" )
                
                problemaTupla = auxilio_resource.find_one_by_id_problema(tuplaChamada[1])
                
                print("sobre o problema: " + problemaTupla[1])
                especificacaoTupla = auxilio_resource.find_one_by_id_especificacao(tuplaChamada[5])
                if especificacaoTupla==None:
                      especificacaoTupla = 'desnecessaria'
                else:
                    print("especificamente: "+ str(especificacaoTupla[1]))
                
                
                cdChamada = tuplaChamada[8]
                print("o codigo dessa chamada:", cdChamada)

    





                
