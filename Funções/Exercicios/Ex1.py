import random 

# Gera um número aleatorio entre 1 e 100
def numeroAleatorio():
    return random.randint(1,100)


def Adivinhacao():
    num = numeroAleatorio()

    palpite = 0
    while palpite is not num:
        palpite = int(input("Adivinhe um número entre 1 e 100: "))
        if palpite > num:
            print("Tente novamente! É um valor menor que ", palpite)
        elif palpite < num:
            print("Tente novamente! É um valor maior que ", palpite)
        else:
            print("Acertou! O número gerado foi ", num)
    
while True:
  Adivinhacao()