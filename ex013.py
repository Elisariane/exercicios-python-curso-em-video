salary = float(input('Qual é o salário do Funcionário? R$ '))
increase = salary + (salary * 15 / 100)
print(f'Um funcionário que ganhava R$ {salary}, com 15% de aumento passa a ganhar R$ {round(increase,2)}')
