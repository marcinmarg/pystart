emails = []

for _ in range(10):
    email = input('Podaj adres email: ')

    if (email.endswith('.pl') or email.endswith('.com')) and '@' in email:
        emails.append(email)

print('Ilosc adresów przed usunieciem duplikatow wynosi: ', len(emails))
emails = set(emails)
print('Ilosc adresów po usunieciu duplikatow wynosi: ', len(emails))

for email in emails:
    print(email)