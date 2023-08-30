# Define the Scrabble letter scores and word bonuses
letter_scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

word_bonuses = {
    'double_letter': 2, 'triple_letter': 3, 'double_word': 2, 'triple_word': 3
}

# Function to calculate the score of a word with bonuses
def calculate_word_score(word, bonuses):
    score = 0

    for letter in word:
        letter = letter.lower()
        if letter in letter_scores:
            score += letter_scores[letter]
    
    for bonus in bonuses:
        if bonus in word_bonuses:
            if bonuses[bonus] > 0:
                if bonus.startswith('double'):
                    score *= word_bonuses[bonus]
                elif bonus.startswith('triple'):
                    score *= word_bonuses[bonus]
                bonuses[bonus] -= 1
    
    return score

# Get user input for the number of words
num_words = int(input("How many words would you like to enter? "))

# Initialize an empty list to store words
words = []

# Get user input for the words
for i in range(num_words):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

# Get user input for bonuses
bonuses = {
    'double_letter': int(input("How many double letter bonuses? ")),
    'triple_letter': int(input("How many triple letter bonuses? ")),
    'double_word': int(input("How many double word bonuses? ")),
    'triple_word': int(input("How many triple word bonuses? "))
}

# Calculate and display scores
total_score = 0
for word in words:
    word_score = calculate_word_score(word, bonuses)
    total_score += word_score
    print(f"Score for '{word}': {word_score}")

print(f"Total score: {total_score}")
