#mostrará o menu principal do programa
def menu():
   
    print("1 - gostaria de relatar um caso de meningite")
    print("2 - gostaria de realizar uma doação")
    print("3 - gostaria me informar sobre casos relatados")
    print("4 - gostaria alterar minhas informações")
    print("5 - gostaria de deletar minhas informações")
    print("6 - sair")
    return int(input('escolha: '))
#mostrará o menu de escolha de informações de um usuario cadastrado em nosso
#banco de dados
def seuUsuario(usuario):
    print("Qual informação gostaria de alterar? ")
    print("[1] peso: ",usuario[2])
    print("[2] comprimento: ",usuario[3])
    print("[3] largura: ",usuario[4])
    print("[4] altura: ",usuario[5])
    print("[5] eixos: ",usuario[6])
    print("[6] placa: ",usuario[7])
    print("[7] marca: ",usuario[8])

def tenhoCadastro():
    print("já possuí cadastro em nosso aplicativo?")
    print("[1] sim já tenho cadastro")
    print("[2] ainda não possuo cadastro")
    