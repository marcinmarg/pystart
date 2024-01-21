from math import  sqrt
a = int(input("Podaj bok trojkata rownobocznego"))
field = a ** 2 * sqrt(3) / 4
print(f'Pole trójkąta równobocznego wynosi {field}.')
print(f'Obwód trójkata rownobocznego wynosi {a * 3}')