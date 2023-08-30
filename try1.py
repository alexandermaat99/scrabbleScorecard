# Define the letter scores according to Scrabble rules
letter_scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Define word and letter multipliers for the board
word_multipliers = {'dl': 2, 'tl': 3}
letter_multipliers = {'dw': 2, 'tw': 3}

def calculate_score(word, letter_bonus={}, word_bonus={}):
    word = word.lower()
    score = 0
    word_multiplier = 1

    for i, letter in enumerate(word):
        letter_score = letter_scores.get(letter, 0)
        letter_multiplier = 1

        if i in letter_bonus:
            letter_multiplier *= letter_bonus[i]

        if i in word_bonus:
            word_multiplier *= word_bonus[i]

        score += letter_score * letter_multiplier

    return score * word_multiplier

# Example usage
word = input("Enter a word: ")
letter_bonus = {1: 2}  # Bonus on the 2nd letter
word_bonus = {0: 3}    # Triple word score on the 1st word

score = calculate_score(word, letter_bonus, word_bonus)
print(f"Score for '{word}': {score}")
