animals = [
    {'name': 'pies', 'breed': 'owczarek niemiecki'},
    {'name': 'kot', 'breed': 'syberyjski'},
    {'name': 'konik polny', 'breed': 'arab'},
    {'name': 'swienia', 'breed': 'dwudzielna'},

]
maxi_lenght = None

for animal in animals:
    lenght = len(animal['name']) + len(animal['breed'])
    if maxi_lenght is None or lenght > maxi_lenght:
        maxi_lenght = lenght

for animal in animals:
    lenght = len(animal['name']) + len(animal['breed'])
    if lenght == maxi_lenght:
        print(animal['name'],  lenght)