letterScores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



# Step 1: Take an input word from the user
input_word = input("Enter a word: ")

# Step 2: Make a list of each individual letter of the word
letter_list = list(input_word)

# Step 3: Ask the user if they want to append to the list
while True:
    print("\nCurrent letter list:", letter_list)
    choice = input("Do you want to append to the list? (yes/no): ").lower()

    if choice == 'yes':
        # Step 4: Allow the user to add or remove letters from the list
        action = input("Do you want to add or remove a letter? (add/remove): ").lower()
        
        if action == 'add':
            letter_to_add = input("Enter a letter to add: ")
            letter_list.append(letter_to_add)
        elif action == 'remove':
            letter_to_remove = input("Enter a letter to remove: ")
            if letter_to_remove in letter_list:
                letter_list.remove(letter_to_remove)
            else:
                print("Letter not found in the list.")
        else:
            print("Invalid action. Please enter 'add' or 'remove'.")
    elif choice == 'no':
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

print("Final letter list:", letter_list)


