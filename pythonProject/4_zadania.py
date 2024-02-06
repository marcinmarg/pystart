names = 'Marcin', 'Tymek', 'MArta', 'Stanislaw', 'Tomek' 'Zuzanna'
for name in names:
    if len(name) > 5:
        print(name)


for counter in reversed(range(1,5)):
    # print(counter)
    for digit in range(1, counter + 1):
        print(digit, end = ' ')
    print()