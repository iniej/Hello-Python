word = input('Enter a word ')
accumulator = ""

word_list = word.split()
for x in range(len( word_list)):
    if x == 0:
        firstword = word_list[x].lower()
        accumulator = accumulator + firstword

    else:
        other_words = word_list[x]
        first_letter = other_words[0].upper()
        other_letters = other_words[1:].lower()
        the_word = first_letter + other_letters

        accumulator = accumulator + the_word







print(accumulator)
