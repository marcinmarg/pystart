from math import  sqrt, ceil

number = 1116548945616787895646513215413156
is_prime = True
for div in range(2, ceil(sqrt(number))+1):
    if number % div == 0:
        is_prime = False
        break

if is_prime:
    print('Liczba jest pierwsza')
else:
    print('Liczba nie jest pierwsza')

