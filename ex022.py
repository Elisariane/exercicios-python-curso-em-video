name = str(input('Digite o seu nome completo:')).strip()

print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras')
print(f'Seu primeiro nome tem {name.find(" ")} letras')
