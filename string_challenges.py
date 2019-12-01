# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1] + "\n")

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f'{len(word)}  \n')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = 'ауеоэяиюыё'
count = 0
for letter in vowel:
    count += word.lower().count(letter)
print(f'{count} \n')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
letters = sentence.split()
print(f'{len(letters)} \n')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
letters = sentence.split()
for first_letter in letters:
    print(f'{first_letter[0]}')
print()

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
letters = sentence.split()
words_len = 0
for first_letter in letters:
    words_len += len(first_letter)
middle = words_len / len(letters)
print(int(middle))
