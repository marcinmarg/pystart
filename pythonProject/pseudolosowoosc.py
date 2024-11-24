from random import choice

options = ('papier', 'kamien', 'nozyce')
computer_choice = choice(options)
print('Wybierz opcje')
user_input = int(input('Ktora opcje wybierasz')) - 1
if user_input not in(0, 1, 2):
    print('Dokonałeś żlego wyboru')
    quit()

user_input = options[user_input]

print(f'Uzytkownik wybral {user_input}.')
print(f'Komputer wybral {user_input}.')

