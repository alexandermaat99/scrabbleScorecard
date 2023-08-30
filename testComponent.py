#this function doubles the score of a certian letter that can be found in the letter_scores dictionary


letter_scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def doubleLetter(letter):
    letter = letter.lower()  # Convert to lowercase to handle uppercase inputs
    if letter in letter_scores:
        return letter_scores[letter] * 2 
    else:
        return 0  # Return 0 if the letter is not found in the dictionary

user_letter = input("Enter a letter: ")
score = doubleLetter(user_letter)

print(f"The score of '{user_letter}' is {score}")




