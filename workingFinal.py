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

#this calculates the double bonus points
def doubleScore(letters):
    bonuses = 0
    for letter in letters:
        letter = letter.lower()  # Convert to lowercase to handle uppercase inputs
        bonuses += letterScores.get(letter, 0) * 2
    return bonuses

#this calculates the tripple bonus points
def trippleLetter(letters):
    bonuses = 0
    for letter in letters:
        letter = letter.lower()  # Convert to lowercase to handle uppercase inputs
        bonuses += letterScores.get(letter, 0) * 3
    return bonuses

#validation for double letters
word = input("Enter a word: ")

#blank tile edit try make this but have it remove the letters from the world
decrease = input("Which letters are blank tiles?: ")
if decrease == "":
    Bdecrease = 0
else:
    Bdecrease = 0
    for letters in decrease:
        letters = letters.lower()
        Bdecrease += letterScores.get(letters, 0)

testD = input("Which letters would you like to double? ")
for letter in testD:
    letter = letter.lower()
    if letter in word.lower():
        lettersD = testD
    else:
        "\n"
        print("Letters not in word")
        lettersD = ""
        "\n"
if testD == "":
    lettersD = ""

#validation for tripple letters
testT = input("Which letters would you like to tripple? ")
for letter in testT:
    letter = letter.lower()
    if letter in word.lower():
        lettersT = testT
    else:
        print("\n Letters not in word \n")
        lettersT = ""
if testT == "":
    lettersT = ""

#finds multiplier for case of double or tripple word bonuses
multiplier = input("Is there a double word bonus?: (Y/N)").lower()
if multiplier == "y":
    multiply = 2
elif multiplier != "y":
    tMultiply = input("Is there a tripple word bonus? (Y/N): ").lower()
    if tMultiply == "y":
        multiply = 3
    else: 
        multiply = 1
else: 
    multiply = 1

#number crunch
wordScore = calculate_score(word) - Bdecrease
doubleScore = doubleScore(lettersD)
trippleScore = trippleLetter(lettersT)
finalScore = (wordScore) + (doubleScore/2) + ((trippleScore/3)*2)
ultimateScore = (finalScore * multiply)

#result print
print(f"The score for the word {word} is: {wordScore}")
print(f"The score for the double bonuses is {doubleScore}")
print(f"The score for the tripple bonuses is {trippleScore}")
print(f"\nYour word score is {finalScore}")
print(f"Your total score is {ultimateScore}\n")