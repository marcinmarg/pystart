fruits = {
    'banan': 8,
    'jablka': 5,
    'pomarancze': 4,
    ' kiwi': 8,
}
# print(fruits['jablka'])

for  fruit in fruits:
    if fruit in ('jablka', 'banan'):
        print(fruits[fruit])

for  fruit in ('jablka', 'banan'):
    print(fruits[fruit])