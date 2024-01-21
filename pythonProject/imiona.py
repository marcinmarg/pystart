notes = 4, 5, 6, 5, 6, 4

print('Oceny ucznia', sorted(notes))

average = sum(notes) / len(notes)

print(f'Srednia ocen {average:.2f}')

if average >= 4.7:
    print('MAsz swiadectow z paskiem')
else:
    print("Sprobuj za rok")
