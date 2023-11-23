import random
repetidas = []
repetidasChamadas = []
def ids():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 8:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidas.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidas.append(num)
    
    return num

def idsChamadas():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 8:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidas.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidasChamadas.append(num)
    
    return num