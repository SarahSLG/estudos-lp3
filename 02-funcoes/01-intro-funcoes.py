# FUNÇÃO
# função é bom para reuso
# Tem que saber sobre abstração (legibilidade) 

# Quero somar uma lista de números
# usar a função sum()

# Quero calcular média de notas dos alunos 
# 1. Tem no Pyhton?
# 2. Alguém já programou? (copiar ou adicionar dependência)
# 3. Declarar 


# 1. DECLARAÇÃO 
# def nome_funcao(parâmetro1, parâmetro2)
#   return valor 

# 2. CHAMADA
# chamando uma função
print('Olá')
sum([1,3,5])
# nome_funcao('dad', 1)

# Função SEM retorno e SEM parâmetros 
# 
def imprimir_mensagem():
    print('Socorro!')

imprimir_mensagem()
imprimir_mensagem()

# Função SEM retorno COM parâmetros
# parâmetros vs argumentos
# parâmetro(da declaração): variável que tem acesso dentro da função, coloca entre parenteses
# argumeto(da chamada): valor que passa para um parâmetro 


def saudacoes(nome):
    print(f'bom dia{nome}')

# argumento para parâmetro nome 'Maria'
saudacoes('Maria')

# argumento para parâmetro nome 
nome_completo = 'José'
saudacoes(nome_completo)

# Função COM retorno SEM parâmetros

def obter_mensagem():
    return 'Socorro'

mensagem = obter_mensagem()
print(mensagem)
print(obter_mensagem())

# Função COM retorno COM parâmetros

def gerar_saudacao(nome):
    return(f'Bom dia {nome}')
print(gerar_saudacao('Pedro'))
print(gerar_saudacao('Sarah'))

# Retorno   parâmetros 
#   não        não
#   não        sim
#   sim        não
#   sim        sim  (adequado) (função pura - sempre devolve o mesmo resultado)

# Em Java não colocar scanner dentro da classe, não ajuda no reuso 
# Imprir saudacao 
# saudacao = frase(dinâmica) + nome da pessoa(dinâmico)
# "Bom dia Pedro"
# "Boa tarde Maria"
# "Boa noite Maria"

def saudacao(nome, frase):
    print(f'{frase} {nome}')

saudacao('Joao', 'Bom dia')

def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao('Joao', 'Bom dia'))

# Reuso 
# enviar email saudacao 
# criar uma carta em pdf 

# código que recebe listas de notas de alunos e imprime uma lista com a média de cada aluno:
# Quebre o problema 

# Entrada
notas_alunos = [
    [9.0, 3.0,7.0],
    [10.0, 3.0,7.0],    
    [0.0, 1.0,3.0],   
]

# Saida [5.5, 1.0, 6.6]
def calcular_media(notas):
    return sum(notas) / len(notas)

# print(calcular_media([0.0, 1.0,3.0]))

def calcular_media_alunos(notas_alunos):
    medias = []

    for notas in notas_alunos:
        media = calcular_media(notas)
        medias.append(calcular_media(notas))

    return medias
    # compreensão de listas 
    # return [calcular_media(notas) for notas in notas_alunos]


calcular_media(notas_alunos)

todas_as_notas = [
    [9.0, 3.0,7.0],
    [10.0, 3.0,7.0],    
    [0.0, 1.0,3.0],   
]


def imprimir_medias(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    print(medias) # não é pura pq tem o print e não return

def enviar_medias_por_email(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    # logica de enviar por email as medias

imprimir_medias(todas_as_notas)
enviar_medias_por_email(todas_as_notas)

# Argumentos nomeados

def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao('Joao', 'Bom dia')) # passagem de parametros posicionais
print(saudacao(nome = 'Joao', frase = 'Bom dia')) # Dessa forma não fica preso a ordem (argumento nomeado)
print(saudacao('Joao', frase = 'Bom dia')) # ao contrário não da certo
# print(saudacao(frase = 'Boa tarde', 'Joao')) # errado!!

# parâmetro com valor padrão (default)

def saudacao(nome, frase = 'Bom dia'):
    return f'{frase} {nome}'

print('Joao') # vai assumir bom dia Joao por causa do valor padrão default
print('Joao', 'Boa tarde')