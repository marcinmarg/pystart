animals = {
    'pies': 4,
    'kto': 4,
    'krowa': 5,
    'swinia': 8,
    'koza': 2,
    'zyrafa': 9,
    'pajak': 6,
    'mrowka': 3,
}

max_number_legs = 0
for animal in animals:
    if animals[animal] > max_number_legs:
        max_number_legs = animals[animal]
print(max_number_legs)

for animal in animals:
    if animals[animal] == max_number_legs:
        print(animal, animals[animal])