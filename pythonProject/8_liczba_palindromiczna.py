value = input('Podaj liczbe')

if value == value[::-1]:
    print("Liczba jest palindromiczna")
else:
    print('Liczba nie jest palindromiczna')

if len(value) % 2 ==0 and int(value) % 11 == 0:
    print("Liczba jest palindrowmiczna")