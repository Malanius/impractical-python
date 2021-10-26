import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
palindrome_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindrome_list.append(word)

print(palindrome_list)