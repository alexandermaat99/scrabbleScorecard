
letterScores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

#function that takes the list of letters and scores them, can be used for every lsit change
def calculateWord(word):
    wordScore = 0 
    for letter in letter_list:
        letter = letter.lower()
        wordScore += letterScores.get(letter, 0)
    return wordScore


#user input to gather the initial letters 
input_word = input("Enter a word: ")

#turns the user reply into a list of words
letter_list = list(input_word)

print(letter_list)


#this removes blank tiles from the score, only two blank tiles possible, might want to change
blank = list(input("Which letters are blank tiles?: "))

for letter in blank:
    if blank == "":
        blank = ""
    else:
        letter_list.remove(letter)

#this applies double letter bonus, needs user validaton to make sure the letter is in the list
double = list(input("Which letters are on a double bonus?: "))

for letter in double:
    if double == "":
        double = ""
    else:
        letter_list.append(letter)

#this applies tripple letter bonuses,needs user validaton to make sure the letter is in the list
tripple = list(input("Which letters are on a tripple bonus?: "))

for letter in tripple:
    if tripple == "":
        tripple = ""
    else:
        letter_list.append(letter)
        letter_list.append(letter)

doubleWord = input("Is there a double word bonus? (Y/N) ").lower()
double_list = []


if doubleWord == "y":
    double_list = []
    for letter in letter_list:
        double_list.extend([letter, letter])
    print(double_list)
elif doubleWord == "n":
    trippleWord = input("Is there a triple word bonus? (Y/N) ").lower()
    if trippleWord == "y":
        triple_list = []
        for letter in letter_list:
            triple_list.extend([letter, letter, letter])
        print(triple_list)
else:
    print("Oops")



#calcualtes the inital score by applying the function to the list of letters 
initialScore = calculateWord(input_word)

print(letter_list)
print(initialScore)