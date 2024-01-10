width = float(input("Largura da parede: "))
height = float(input("Altura da parede: "))

area = width * height
total_ink = area / 2

print(f'Sua parde tem a dimensão de {width}x{height} e a sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {total_ink}L de tinta')
