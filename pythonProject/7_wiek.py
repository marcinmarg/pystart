current_year = 2024
birth_year = int(input("Podaj rok urudzenia: "))
age = current_year - birth_year

print(f'Twoj wiek to {age}')

if age >= 18:
    print('Jestes dorosły')
else:
    print(f'Bedziesz dorosly za {18 - age} lat')

if birth_year % 4 == 0 and birth_year % 100 != 0 or birth_year % 400 == 0:
    print('Urodziłeś się w przestepnym roku')
