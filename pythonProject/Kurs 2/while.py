bus_capasity = 100
passanger_in_bus = 0

bus_can_start = False
while not bus_can_start:
    passanger_in_bus += int(input('Ile osób weszlo tym razem? '))

    should_start = input('Czy autobus ma juz ruszacz [Yes/No]')
    if should_start == 'Yes':
        bus_can_start == True

    if passanger_in_bus > bus_capasity:
        print(f'Ostatnie {passanger_in_bus-bus_capasity} musi wyjsc, bo nie pojedziemy')

print(f'Autobus rusza')