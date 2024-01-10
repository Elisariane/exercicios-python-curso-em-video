from math import hypot

cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjascente: '))

print(f'A hipotenusa irá medir {round(hypot(cat_op, cat_ad), 2)}')
