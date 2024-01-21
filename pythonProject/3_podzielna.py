value = int(input('Podaj liczbe: '))

if value % 5 == 0 and value % 11 == 0:
    print('Liczba podzielna przez 5 i 11.')
elif value % 5 == 0:
    print('Liczba jest podzielna przez 5. ')
elif value % 11 == 0:
    print('Liczba jest podzielna przez 11. ')
else:
    print('Liczba nie dzieli sie nia przez 5 ani 11')


