from random import choice
capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
    'Słowacja': 'Bratysława',
    'Slowenia': 'Lublana',
    'Chorwacja': 'Zagrzeb',
    'Serbia': 'Belgrad',
}
correct_answers = 0
for _ in range(3):
    selected_coutry = choice(list(capitals.keys()))
    answer = input (f'Jaka jest stolica kraju {selected_coutry}?')
    if answer == capitals[selected_coutry]:
        print('Bardzo dobrze')
        correct_answers += 1
    else:
        print('Sprobuj jeszcze raz ')

if correct_answers = 3:
    print('Poszło Ci bardzo dobrze')
elif correct_answers = 2:
    print('Tylko jeden bład')
elif correct_answers = 1:
    print('Dwa błędy')
else:
    print('Nastepnym razem bedzie lepiej')
