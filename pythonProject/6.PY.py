values = tuple(range(12, 1025, 6))
print('ilosc wartosci', len(values))

print('Trzy pierwsze liczby', values[0:3])

print('przed ostatni', values[-2])

print('co 6', values[3::6])

print('co 3 ', values[::-3])

print('śrenida od konca', sum(values[-10::])/10)
