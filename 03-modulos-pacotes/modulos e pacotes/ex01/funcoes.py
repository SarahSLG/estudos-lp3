def volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def potenciatermostato(volume, tempdesejada, tempambiente):
    return volume * 0.05 * (tempdesejada - tempambiente)

def qtdfiltragem(volume):
    return volume * 3
