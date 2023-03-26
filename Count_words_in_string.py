# Count Words in a String - Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

def count_words(word, separator=' '):
    counter = 0
    word_list = word.split(separator)
    for n in word_list:
        counter += 1
    return counter

print(count_words('Hello,my,name,is,Lukasz,and,I\'m,31,years,old.', ','))
print(count_words('Hello my name is Lukasz and I\'m 31 years old.'))

