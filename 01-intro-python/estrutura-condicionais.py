#if/else
idade = 25

if idade >= 18:
    print('maior de idade')
    print('sdad')
else:
    print('menor de idade')

# if/elif/else
# Criança 0 a12, adolecente 13 a 17
# Adulto 18 a 59, idoso 60+ 
if idade > 0 and idade <= 12:
    print('crianca')
if idade > 12 and idade <= 17:
    print('adolescente')
if idade > 17 and idade <= 59:
    print('Adulto')
if idade > 59:
    print('idoso')

if idade <= 12:
    print('crianca')
elif idade <= 17:
    print('adolescente')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')                

#Condições alinhadas
email = 'adminemail@gmail.com'
senha= '123'

if email == 'adminemail@gmail.com':
    if senha == '123':
        print('liberado')
    else:
        print('erro')
else:
    print('erro')

if email == 'adiminemail@gmail.com' and senha == '123':
        print('liberado')
else:
    print('erro')

# entrada eamil, senha
# saida True or False 
def libera_acesso(amil, senha):
    if email == 'adiminemail@gmail.com' and senha == '123':
        return True
    else:
        return False

def liberar_acesso(email, senha):
     return email == 'adiminemail@gmail.com' and senha == '123'

# entrada hora_atual
# sim ou não 
def dentro_horario_comercial (hora_atual):
    return hora_atual >= 8 and hora_atual <= 18

# dia 1,2,3,4,5,6,7
# palavra doming, segunda, terca, quarta, quinta, sexta, sábado

dia = 3

if dia ==1:
    print('domingo')
elif dia == 2:
    print('segunda')

lista = ['domingo', 'segunda', 'terca', 'quarta', 'quinta']
dia = dia - 1
print(lista[dia])

dias = {
    1: 'domingo' ,
    2: 'segunda' ,
    3: 'terça' ,
}

if dia in dias:
    print(dias[dia])

    #ba ba ba, ba ba, baba, ba ba ba, ba ba, baba

# OPERADOR TERNÁRIO (atribuição de valores por condicional)
idade = 20
# maior ou menor 
status = '' 

# SEM Ternário
if idade >= 18:
    status = 'maior'
else:  
    status = 'menos'

# COM Ternário
status = 'maior' if idade >= 18 else 'menor'

# MATCH (switch avançado do python)
# _ (caso default)
match dia:
        case 1:
            print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case _:
            print('Dia inválido')


match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
    case _:
        print('Dia inválido')

# Documentação do match    
# https://peps.python.org/pep-0622/

