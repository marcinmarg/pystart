dictionary = {
    'dog': 'pies',
    'cat': 'kot',
    'cow': 'krowa',
    'chicken': 'kurczak'
}

option = int(input('Z jakiego jezyka tlumaczymy? [eng-pl]- 1: , [pol-eng]-2: '))
if option not in [1, 2]:
    print('Nie wiem co chces zrobic.')
    quit()

word = input(' Jakie słowo mam przetlumaczyc: ')
translated_word = None
for english_word, polish_word in dictionary.items():
    if option  == 1 and  english_word == word:
        translated_word = polish_word
        break

    elif option == 2 and polish_word == word:
        translated_word = english_word
        break
if translated_word is not None:
    print(f'Tłumacznie to {translated_word}')
else:
    print('Nie znam tego słowa.')

