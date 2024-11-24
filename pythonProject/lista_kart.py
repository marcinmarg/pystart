from  random import  choices, shuffle
colors = [chr(9824), chr(9827), chr(9829), chr(9830)]
values = list(range(2, 11)) + ['J', 'K', 'Q', 'A']
cards = []

for color in colors:
    for value in values:
        cards.append(f'{value}{color}')

print(choices(cards, k=2))
shuffle(cards)
print(cards[:2])
print(cards.pop(), cards.pop())