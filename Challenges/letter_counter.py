def letter_counter(word):
    word = word.lower()
    def counter(letter):
        return word.count(letter)
    return counter

counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1 