"""Convert any english word to pig latin."""

VOWELS = 'aeiouy'

def pig_latinize(word):
    """Convert given word to pig latin."""
    if word[0] in VOWELS:
        return word + "way"
    return word[1:] + word[:1] + "ay"

def main():
    """Promts for word to be converted to pig latin."""
    word = input("Pick a word to convert to pig latin: ").lower()
    pig_latin_word = pig_latinize(word)
    print(f"Your word in pig latin: {pig_latin_word}")

if __name__ == "__main__":
    main()
