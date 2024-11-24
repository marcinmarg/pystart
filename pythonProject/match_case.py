day_numbe = int(input('Podaj numer dnia tygodnia '))

day_tex_number = None
match day_numbe:
    case 1: day_tex = 'poniedzialek'
    case 2: day_tex = 'wtorek'
    case 3: day_tex = 'sroda'
    case 4: day_tex = 'czwartek'
    case 5: day_tex = 'piatek'
    case 6: day_tex = 'sobota'
    case 7: day_tex = 'niedziela'
    case _:
            print('Nie ma takiego dnia')
            quit()

print(f'Podany dzien {day_tex}')




