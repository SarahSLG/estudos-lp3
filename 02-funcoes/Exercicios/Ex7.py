from palavraforca import palavra
letras_usuario = []
chances = 7
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print('_', end=" ")
    print(f"Voce possui {chances} chances")
    tentativa = input("Escolha uma letra: ")
    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances = chances - 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou == True:
        break


if ganhou:
    print(f"Prabens, voce ganhou. A palavra era: {palavra}")
else:
    print(f"Você perdeu, a palavra era: {palavra}")

