print('Caesar Cipher program')
characters = list(map(chr, range(48, 127)))
characters.append(' ')
print(characters)

def decoding(your_word):
    new_word = ''
    for char in your_word:
        index_num = characters.index(char)
        new_index = index_num+25
        if new_index > len(characters):
            new_index -= len(characters)
        new_word += characters[new_index]
    return new_word

def encoding(your_word):
    new_word = ''
    for char in your_word:
        index_num = characters.index(char)
        new_index = index_num - 25
        new_word += characters[new_index]
    return new_word

program_on = True
while program_on:
    what_do = input('What do you want to do: decode, encode, exit').lower().strip()
    if what_do == 'decode':
        your_word = input('type a word')
        new_word = decoding(your_word)
        print(new_word)
    elif what_do == 'encode':
        your_word = input('type a word')
        new_word = encoding(your_word)
        print(new_word)
    elif what_do == 'exit':
        print('good bye!')
        program_on = False
    else:
        print('this function is not exists')
        continue