num = int(input('Digite um número: '))

for cont in range(1,11):
    print('{} x {:2} = {}'.format(num, cont, num*cont))

# {:2} - deixa dois digitos nos numeros do cont na tabuada