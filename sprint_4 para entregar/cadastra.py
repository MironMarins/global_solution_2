


def cadastraDoacao(id,data,nome):
    
    D = {}
    
    D['idUsuario'] = id
    
    aux = float(input("escreva o valor que gostaria de doar(0.0)? "))
    D['valor'] = aux

    aux = str(input("Qual a forma de pagamento? "))
    D['forma'] = aux

    D['data'] = data
    D['usuario'] = nome
    return D

def seuVeiculo(idveiculo,id,placa,marca,peso,comprimento,largura,altura,eixos,data):
    V = {}
    V['idveiculo'] = idveiculo
    V['id'] = id
    V['placa'] = placa
    V['marca'] = marca
    V['peso'] = peso
    V['comprimento'] = comprimento
    V['largura'] = largura
    V['altura'] = altura
    V['eixos'] = eixos
    V['data'] = data
    return V

def cadastraCliente(data):
    
    cliente = {}
    aux = str(input("informe seu nome completo: "))
    cliente['nome'] = aux

    aux = str(input("informe seu CPF(numeros apenas): "))
    cliente['cpf'] = aux
    aux = str(input("informe seu RG(numeros apenas): "))
    cliente['rg'] = aux
    aux = str(input("sua data de nascimento(DD/MM/YYYY): "))
    cliente['nascimento'] = aux
    
    print("seu sexo biologico")
    print("(M) masculino")
    print("(F) feminino")
    aux = str(input())
    cliente['sexo'] = aux
    aux = str(input("estado civil: "))
    cliente['estadoCivil'] = aux
    aux = str(input("seu grupo sanguineo: "))
    cliente['sangue'] = aux
    aux = str(input("agora nos informe qual o seu login de usuario: "))
    cliente['login'] = aux
    aux = str(input("por ultimo insira uma sua senha de para seu login: "))
    
    cliente['senha'] = aux
    cliente['data'] = data

    
    #veiculos.append(cadastraV())
    #cliente['veiculos'] = veiculos
    #idCliente = cliente['id']
    #listaIdCliente.append(idCliente)
    return cliente
usuario = cadastraCliente(data="dsgfh")

print(usuario)
def seuCadastro(id,nome,cpf,data):
    cli = {}
    cli['CodigoCliente'] = id
    cli['nome'] = nome
    cli['cpf'] = cpf
    cli['data'] = data
    return cli

def carga(placa,data,codigo):
      
    Carga = {} 
    
    Carga['placa'] = placa

    aux = float(input("Quanto sua carga pesa em toneladas (0.0): "))
    Carga['peso'] = aux

    aux = float(input("Quanto sua carga mede em comprimento em metros(0.0): "))
    Carga['comprimento'] = aux

    aux = float(input("Qual a altura de sua carga em metros (0.0): "))
    Carga['altura'] = aux

    aux = float(input("Qual a largura de sua carga em metros (0.0): "))
    Carga['largura'] = aux

    aux = int(input("quantos eixos sua carga possui: "))
    Carga['eixos'] = aux

    aux = str(input("por ultimo, qual o tipo de carga externa que seu veiculo esta carregando: "))
    Carga['CargaTipo'] = aux
    
    Carga['data'] = data
    Carga['codigo'] = codigo   
    return Carga

def suaCarga(placa,peso,comprimento,largura,altura,eixos,tipo,data,codigo):
    V = {}
    V['placa'] = placa
    V['peso'] = peso
    V['comprimento'] = comprimento
    V['altura'] = altura
    V['largura'] = largura
    V['eixos'] = eixos
    V['CargaTipo'] = tipo
    V['data'] = data
    V['codigo'] = codigo
    return V




