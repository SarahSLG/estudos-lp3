from funcoes import volume, potenciatermostato, qtdfiltragem


comprimento = float(input('Digite o comprimento\n'))
largura = float(input('Digite a largura\n'))
altura = float(input('Digite a altura\n'))
tempdesejada = float(input('Digite a temperatura desejada da água\n'))
tempambiente = float(input('Digite a temperatura ambiente da água\n'))

volume = volume(comprimento, altura, largura)
print('o volume é ', volume)
potenciatermostato = potenciatermostato(volume, tempdesejada, tempambiente)
print('A potência do termostato necessária para manter a temperatura adequada dentro do aquário é ', potenciatermostato)
qtdfiltragem = qtdfiltragem(volume)
print('A quantidade em litros de filtragem por hora necessária para manter a qualidade da água é ' , qtdfiltragem)
