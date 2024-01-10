price = float(input('Qual é o preço do produto? R$ '))
discount = price - (price * 5 /100)
print(f'O produto que custava R${price}, na promoção com desconto de 5% vai custar R$ {round(discount, 2)}')
