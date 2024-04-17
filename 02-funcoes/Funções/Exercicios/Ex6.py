pontuacao = (int(input ("Digite sua pontuação")))

if pontuacao >= 90:
    print ("A")
elif pontuacao >= 80 and pontuacao < 89:
    print ("B")
elif pontuacao >= 70 and pontuacao < 79:
    print ("C")
elif pontuacao >= 60 and pontuacao < 69:
    print ("D")
else:
    print ("F")