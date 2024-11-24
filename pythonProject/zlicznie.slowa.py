sentence = 'Python jest szybki Python to wspanialy jezyk szybki i wydajny'
words = sentence.split(' ')
word_counter = {}

for word in words:
 word_counter.update({word: word_counter.get(word, 0) + 1})
print(word_counter)