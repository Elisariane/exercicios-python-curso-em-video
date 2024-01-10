from math import sin,cos,tan, radians

number = float(input('Digite o ângulo que deseja: '))
print(f'O ângulo de {number} tem o SENO de {sin(radians(number)):.2f}')
print(f'O ângulo de {number} tem o COSENO de {cos(radians(number)):.2f}')
print(f'O ângulo de {number} tem a TANGENTE de {tan(radians(number)):.2f}')
