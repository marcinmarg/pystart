person = ('John', 'Smith', 50)
print(f'Imie: {person[0]}')
print(f'Nazwisko: {person[1]}')
print(f'Wiek: {person[2]}')

print('___' *30)
calculations = (1, 2, 3), (4, 5, 6), (7, 8, 9)
for calculation in calculations:
    print(f'{calculation[0]} + {calculation[1]}+ {calculation[2]} = {sum(calculation)}')