frase = str(input('Digite uma palavra ou frase: ')).strip().upper() # deixa maiuscula e tira os espaços
palavras = frase.split() # separa a frase em palavras
junto = ''.join(palavras) # junta as palavras sem espaço
inverso = ''
for letra in range(len(junto) -1, -1, -1): # pega o numero de letras do junto e tira 1, vai ate a letra antes da primeira e vai voltando uma letra
    inverso = inverso + junto[letra]
if inverso == junto: # compara a palavra ou frase no sentido normal e no inverso
    print('Palindromo')
else:
    print('Não é um palindromo')