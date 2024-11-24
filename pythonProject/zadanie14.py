#zadanie 1


# zadanie 2

number_of_numbers = 5
list_of_numbers = []
for counter in range(5):
    value = int(input(f'Podaj liczbe: {counter + 1} / {number_of_numbers}: '))
    list_of_numbers.append(value)

print('Najmniejsza liczba to:', min(list_of_numbers))
print('Najwieksza liczba to:', max(list_of_numbers))
print('średnia liczba to:', sum(list_of_numbers) / number_of_numbers)

# Zadanie3

