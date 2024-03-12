#Operadores aritméticos 
# +, - , *, / , ** (potenciação)
nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3  #mesmo que a precedencia seja correta é uma boa prática colocar os parenteses

# número elevado a outro
# e elevado n
# 10 elevado a 2
numero = 10
numero_elevado_2 = numero * numero
numero_elevado_2 = numero ** 2

# Operadores lógicos
# and, or, not
print(3 + 2) #5
print(True and True) # AND devolve um boolean #True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

# permitir a entrada nas condições:
# - o suário for funcionário 
# - usuário não estiver bloaqueado 
# - a hora atual estiver entre 8h e 18h

# permitir entrada a qualquer momento e forma:
# admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False 
horario_comercial = hora_atual >= 18 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado
# variaveis que armazenam booleanos
# Exemplo
horario_comercial = 17 >= 8 and 17 <= 18
horario_comercial = True and True


#if(usuario_funcionario == True)
# quando é boolean não precisa compara-las

if  usuario_admin or (funcionario_ativo and horario_comercial and hora_atual >= 8 
and hora_atual <= 18):

    print('acesso permitido')

idade = 22

maior_idade = idade >= 18

if maior_idade:
    pass #significada "desconsidere isso aqui" - quando não tem conteúdo para esse bloco


# Operadores de comparação
# ==, !=,>, <, >=, <=

idade = 25
maior_idade >= 18 #True

nota1 = 10.0
nota2 = 5.5
nota3 = 7.5
media = (nota1 + nota2 + nota3) / 3

if media >= 6.0:
    print('aprovado')

# igual o de cima feito sem >=
if media > 6.0 or media == 6.0:
    print('aprovado')


# is, is not
# Operador de identidade
# comparar se os objetos ocupam o mesmo
# espaço de memória 

a = [1,2,3] 
b = [1,2,3]
print(a == b) # True
print(a is b) # False

c = b # criamos uma variável c que aponta para a variável b
print(b is c) # True

# Operador in, not in
# verificar se um elemento existe ou não em uma sequência
# str, list, tuple
opcoes = ('sim', 'nao','talvez')
opcao = input('Digite uma opção') 

# Torna o programa menos sujeito a erro:
opcao = opcao.lower() # mais flexivel, coloca em letra minuscula 
opcao = opcao.strip() # tira espaços


# verifica se uma opcao está dentro de opcoes
if opcao in opcoes:
    print('ok')
else:
    print('nao tem essa opcao')

# Outra solução 
# opcoes = {
#    "sim": ['s', 'y', 'yes', 'sim'],
#    "não": ['n', 'no', 'nao'],
# }

numeros = [1, 3, 5, 6]
# in no contexto do for não devolve booleano
# in no for devolve o valor da lista que tá interando
for numero in numeros:
    print(numero)

