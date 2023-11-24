


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
    return cliente

def seuCadastro(id,nome,rg,cpf,login,senha,nascimento,sexo,estadoCivil,sangue,data):
    cli = {}
    cli['id'] = id
    cli['nome'] = nome
    cli['cpf'] = cpf
    cli['rg'] = rg
    cli['login'] = login
    cli['senha'] = senha
    cli['nascimento'] = nascimento
    cli['sexo'] = sexo
    cli['estadoCivil'] = estadoCivil
    cli['sangue'] = sangue
    cli['data'] = data
    cli['nome'] = nome
    return cli






