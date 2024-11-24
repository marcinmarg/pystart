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
selected_coutry = choice(list(capitals.keys()))
answer = input (f'Jaka jest stolica kraju {selected_coutry}?')
if answer == capitals[selected_coutry]:
    print('Bardzo dobrze')
else:
    print('Sprobuj jeszcze raz ')