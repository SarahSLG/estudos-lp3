from funcoes import imc, peso_normal, classificacao

peso = float(input('Digite seu peso em Kg\n'))
altura = float(input('Digite sua altura\n'))

imc = imc(peso, altura)
classificacao = classificacao(imc)
print('Sua classificação é ', classificacao)
peso_normal = peso_normal(imc)
peso_normal(imc)
