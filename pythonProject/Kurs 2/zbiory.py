from random import choice
items = ['latarka', 'linka', 'zegraek', 'ladowarka', 'kluczyk', 'miecz']

player_items = set()

for _ in range(10):
    item = choice(items)
    print(f'Znalazlem {item}')
    if item in player_items:
        print('Ten przedmiot juz zebralem')

    player_items.add(item)

print(player_items)
