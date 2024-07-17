def imc(peso, altura):
    return peso / (altura * altura)
    
def peso_normal(imc):
    if imc < 24.90:
        diferenca = 24.90 - imc
        print(f'É necessário ganhar {diferenca:.2f}')
    elif imc > 24.90:
        diferenca = imc - 24.90
        print(f'É necessário perder {diferenca:.2f}')
    else:
        print('Você possui o peso ideal')

def classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"
