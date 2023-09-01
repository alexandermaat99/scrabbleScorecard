letterScores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


#this calculated the total point of the word minus the bonuses
def calculate_score(word):
    wordScore = 0
    for letter in word:
        letter = letter.lower()  # Convert letter to lowercase to handle both upper and lower case letters
        wordScore += letterScores.get(letter, 0)  # Get the score for the letter from the dictionary, default to 0 if not found
    return wordScore

#this calculates the bonus points
def doubleLetter(letters):
    bonuses = 0
    for letter in letters:
        letter = letter.lower()  # Convert to lowercase to handle uppercase inputs
        bonuses += letterScores.get(letter, 0) * 2
    return bonuses
        

word = input("Enter a word: ")
test = input("Which letters would you like to double? ")
for letter in test:
    letter = letter.lower()
    if letter in word.lower():
        letters = test
    else:
        "\n"
        print("Letters not in word")
        letters = ""
        "\n"
if test == "":
    letters = ""
    


wordScore = calculate_score(word)
bonusScore = doubleLetter(letters)
finalScore = wordScore + (bonusScore/2)



print(f"The score for the word {word} is: {wordScore}")
print(f"The score for the bonuses is {bonusScore}")

print(f"\n Your total score is {finalScore}\n")

