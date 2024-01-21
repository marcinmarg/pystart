value = int(input('Podaj czas w sekundach'))
hour = value // 3600
minuts = value % 3600 / 60

print(f'{hour:02.0f}:{minuts:02.0f}')
