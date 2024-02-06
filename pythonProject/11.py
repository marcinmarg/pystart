sentence = 'Litwo ojczyzno moja Ty jestes jak zdrowie...'
for word in sentence.split(' '):
    if word[0].lower() == word[-1].lower():
        print(word)

new_sentence = ''
vowels = 'aeiouyąę'

for char in sentence:
    if  char.lower() not in vowels:
        new_sentence += char
print(new_sentence)