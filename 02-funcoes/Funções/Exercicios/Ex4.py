def votacao (): 
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    print('Claudete vote 1 \ Sarah Sabonete vote 2 \ Alison Jorjao vote 3')
    for c in range (7):
        voto = int(input("Digite o número do seu candidato: "))
        match voto:
            case 1:
                candidato1 = candidato1 +1  
            case 2:
                candidato2 = candidato2 +1
            case 3:
                candidato3 = candidato3 +1


    ganhador = candidato1 # armazena o maior numero, ou seja, o candidato que receber maior voto
    if (candidato2 > ganhador):
        ganhador = candidato2 
    if (candidato3 > ganhador):
        ganhador = candidato3
        
    if ganhador == candidato1:
        print('Eleita: Claudete')
    elif ganhador == candidato2:
        print('Eleita: Sarah')
    else:
        print('Eleito: Alison')

    print ('numero de votos: candidato 1:', candidato1, ' candidato 2:', candidato2, ' 2candidato 3:',candidato3)
votacao()