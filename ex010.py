money = float(input('Quanto dinheiro você tem na carteira? R$ '))
real_to_dolar = money / 4.91
print(f'Considerando que US$ 1,00 = R$ 4,91 com R$ {money} você pode comprar {round(real_to_dolar,2)}')
