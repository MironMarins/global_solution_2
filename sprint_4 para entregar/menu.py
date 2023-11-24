#mostrará o menu principal do programa
def menu():
   
    print("1 - gostaria conferir os maiores doadores")
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
    print("[1] nome: ",usuario[1])
    print("[2] login: ",usuario[4])
    print("[3] senha: ",usuario[5])
    print("[4] estado civil: ",usuario[8])
    

def tenhoCadastro():
    print("já possuí cadastro em nosso aplicativo?")
    print("[1] sim já tenho cadastro")
    print("[2] ainda não possuo cadastro")
    