days = int(input('Digite quantos dias de aluguel: '))
km = float(input('Digite quantos KM foram rodados: '))

price_for_days = 60 * days
price_for_km = 0.15 * km 
total = price_for_days + price_for_km

print(f'O total a pagar é de R$ {round(total,2)}')
