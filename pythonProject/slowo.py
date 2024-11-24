from random import choice, shuffle
words = ['widzmin', 'kompas', 'slonecznik', 'gruszka', 'wulkan', 'orzel']
selected_word = choice(words)
letters = list(selected_word)
shuffle(letters)
print('Słowo do odgadnięcia to: ', ''.join(letters))
for number_tries in range(3):
    answer = input('Czy wiesz jakie to slowo?: ')
    if answer == selected_word:
        print(f'Brawo zgadles potrzebowales { number_tries+1 } prob')
        break
    else:
        print('Sprobuj jeszcze raz')
#print(shuffle(list(word)))
