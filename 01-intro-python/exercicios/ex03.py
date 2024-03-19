# ex03 - Crie um programa em Pyhton que recebe como entrada 
# o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:
#    compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
#    compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
#    compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
#    compras iguais ou superiores a R$ 500,00 - 15% de desconto

valorCompra = float(input('Digite o valor da compra'))

if valorCompra >= 0.01 and valorCompra <= 9.99:
    print(valorCompra) 

elif valorCompra >= 10.00 and valorCompra <= 99.99:
    desconto = valorCompra * 0.05
    ValorFinal = valorCompra - desconto
    print(ValorFinal, desconto)

elif valorCompra >= 100.00 and valorCompra <= 499.99:
    desconto = valorCompra * 0.10
    ValorFinal = valorCompra - desconto
    print(ValorFinal, desconto)

else:
    desconto = valorCompra * 0.15
    ValorFinal = valorCompra - desconto
    print(ValorFinal, desconto)        


        