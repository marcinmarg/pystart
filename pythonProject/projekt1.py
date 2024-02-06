from math import  ceil
walls = int(input('Ile jest scian do pomalowania ? '))

print('Wszystkie pomalowanie scainy w metrach np 3.2 ')
previsous_height = 3
total_area = 0

for counter in range(walls):
    width = float(input(f'Podaj mi szerokosc sciany nr {counter +1}: '))
    height = input(f'Podaj mi wysokosc sciany nr {counter + 1}: ')

    if height == '':
        height = previsous_height
    else:
        height = float(height)
        previsous_height = height

    total_area += height * width

print(f'Scian do pomalowania {total_area}')

layers_of_base = int(input('Warstwy gruntu: '))
layers_of_paint = int(input('Warstwy farby: '))

liters_of_base = ceil(layers_of_base * total_area / 5)
liters_of_paint = ceil(layers_of_paint * total_area / 13)

print(f'Potrzebujesz listrów gruntu: {liters_of_base}. ')
print(f'Potrzebujesz listrów farby: {liters_of_paint}. ')


