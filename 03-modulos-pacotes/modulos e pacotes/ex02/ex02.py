from funcoes import imc, peso_normal, classificacao

peso = float(input('Digite seu peso em Kg\n'))
altura = float(input('Digite sua altura\n'))


imc_valor = imc(peso, altura)
classificacao_valor = classificacao(imc_valor)
print('Sua classificação é', classificacao_valor)
peso_normal(imc_valor)
