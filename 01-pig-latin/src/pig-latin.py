consonants = ["b","c","d","f","g","j","k","l","m","n","p","q","s","t","v","x","z","h","r","w","y"]

def pig_latinize(word):
    start_letter = word[:1]
    rest_word = word[1:]
    if start_letter in consonants:
        return rest_word + start_letter + "ay"
    return word + "way"

def main():
    word = input("Pick a word to convert to pig latin: ").lower()
    pig_latin_word = pig_latinize(word)
    print(f"Your word in pig latin: {pig_latin_word}")

if __name__ == "__main__":
    main()
