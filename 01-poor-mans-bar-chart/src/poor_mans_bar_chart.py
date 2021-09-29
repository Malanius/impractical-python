import pprint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_occurences(sentence):
    graph = {}
    for char in sentence:
        if char not in ALPHABET:
            continue
        if char in graph.keys():
            graph[char] = graph[char] + [char]
        else:
            graph[char] = [char]
    return graph

sentence = input("Intput sentence to analyze: ").lower()
printer = pprint.PrettyPrinter(indent=4)
printer.pprint(count_occurences(sentence))
