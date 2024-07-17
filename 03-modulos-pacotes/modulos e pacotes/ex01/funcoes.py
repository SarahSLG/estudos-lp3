def volume(comprimento, altura, largura):
    (comprimento * altura * largura) / 1000

def potenciatermostato(volume, tempdesejada, tempambiente):
    potencia = volume * 0.05 * (tempdesejada - tempambiente)

def qtdfiltragem(volume):
    filtragem = volume * 3