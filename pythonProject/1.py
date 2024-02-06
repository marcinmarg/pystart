number = int(input("podaj liczbe"))
result = number

for power in range(4):
    result = result * number
    print(f'Liczba {number} podniesieona do potengi {power + 2} wynosi {result}', number ** (power+2))

