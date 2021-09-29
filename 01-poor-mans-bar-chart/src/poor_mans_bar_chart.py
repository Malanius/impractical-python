import pprint
from collections import defaultdict

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_occurences(sentence):
    graph = defaultdict(list)
    for char in sentence:
        if char in ALPHABET:
            graph[char].append(char)
    return graph

sentence = input("Intput sentence to analyze: ").lower()
printer = pprint.PrettyPrinter(indent=4)
printer.pprint(count_occurences(sentence))
