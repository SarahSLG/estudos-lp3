# FOR (ir do zero até o final)
# se quiser ir de par em par no vetor usa range 
palavra ='python'
for letra in palavra:
    print(letra)

numeros = [1, 3, 4, 6, 8]
for numero in numeros:
    print(numero)

#estudante1@debian:~$ python3
#Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> range(5)
#range(0, 5)
#>>> list(range(5))
#[0, 1, 2, 3, 4]

# RANGE 
# range(stop)
# range(5) - 0,1,2,3,4

# range (start, stop)
# range(4,10) - 4, 5, 6, 7, 8, 9

# range(start, stop, step)
# range (3,10,2) - 3,5,7,9

for i in range(10):
    print(i)

# lista = list(range(1001)) - gera numeros até 1000
# type(5) - retorna o tipo

# WHILE

contador = 0
while contador < 5:
    print(contador)
    contador += 1



# BREAK 
# break pula o loop
# enconrtar o primeiro número par

# sai qunado chegar no 4
numeros = [1, 2, 3, 4, 6]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break

# sai da primeira iteração (primeira vez rodado) sai no 1 
numeros = [1, 2, 3, 4, 6]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
    break

# CONTINUE
# pula iteração 
numeros = [0, -3, 1, 2, 3, 4, 6]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

# melhor do que usar o de cima (faz a mesma coisa):
for numero in numeros:
    if numero > 0:
        print(numero)


# compreensão de lista
numeros = [2, 3, 4]
quadrados = [4, 9, 16]

# isso é mapeamento
# append coloca o numero na último indice
# como fazer uma lista dos numeros ao quadrado
for numero in numeros:
    quadrados.append(numero**2)

# isso é filtrar de uma lista
numeros = [1, 3, 4, 5 ,6]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# modelo do pyhton para mapear (equivalente ao de cima sobre os quadrados)
# tá criando uma lista para cada numero em numeros 
# no inicio coloca o que quer fazer com os números
quadrados = [numero ** 2 for numero in numeros]

# modelo do pyhton para filtar
# (equivalente ao de cima sobre os pares)
pares = [numero for numero in numeros if numero % 2 == 0]

# impares 
# impares = [numero for numero in numeros if numero % 2 ! 0]

# Outro exemplo criando uma lista com palavras maiusculas 
palavras = ['ola', 'mundo', 'teste']
palavra2 = [palavra.upper() for palavra in palavras]

