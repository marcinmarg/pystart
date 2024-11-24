from random import choice

options = ('papier', 'kamien', 'nozyce')
computer_choice = choice(options)
print('Dostepne opcje: 1 - papie, 2 - kamien, 3 - nozyce')
user_choice = int(input('Ktora opcje wybierasz?')) - 1

if user_choice not in (0, 1, 2):
    print ('dokonales nieprawidlowego wyboru')
    quit()

user_choice = options[user_choice]

print(f'Uzytkownik wybral {user_choice}.')
print(f'Komputer wybral {computer_choice}.')

if user_choice == computer_choice:
    print('Mamy remis')
elif (user_choice == 'papier' and computer_choice == 'kamien') or \
    (user_choice == 'nozyce' and computer_choice == 'papier') or \
    (user_choice == 'kamien' and computer_choice == 'nozyce'):
    print ('wygral gracz')
else:
    print('wygral komputer')
