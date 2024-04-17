def VerificaVogal(c): # recebe uma letra de STR
    Vogais = "a, e, i, o, u" # lista usada p/ dizer oq é vogal
    if (c in Vogais):
        return True
    else:
        return False
    
def ContaVogais (STR):
    STR = STR.lower () # converte a string p/ minusculo
    STR = STR.strip() 

    qtd = 0 # variavel acumuladora
    for letra in STR: # percorre cada letra da string digitada
        if (VerificaVogal(letra) == True):
            qtd = qtd + 1
    return print('número de vogais: ', qtd)

def Verifica_Consoante(c):
    consoantes = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, y, z"
    if (c in consoantes):
        return True
    else:
        return False

def ContaConsoantes(STR):
    STR = STR.lower () # converte a string p/ minusculo
    STR = STR.strip() 

    qtd = 0 # variavel acumuladora
    for letra in STR: # percorre cada letra da string digitada
        if (Verifica_Consoante(letra) == True):
            qtd = qtd + 1
    return print('número de consoantes: ', qtd)

# Para chamar as funções: 
print(ContaVogais('sarah foi a feira'))
print(ContaConsoantes('sarah foi a feira'))