# Jacob Hardman
# John Minney
# Dr. Miller
# CS 301 
# First Commit: 1/12/2021
# Last Commit: 1/14/2021
# Version: 0.2

### EXTRA FUNCTIONS
def Get_Letter_Set():
    while True:
        letter_set = input('Enter a String of 6 characters: ').lower()
        if len(letter_set) == 6:
            return letter_set
        else:
            print('Only a String of 6 characters are allowed...')

def Is_Letter_In_String(letters, word):
    letter_check = [characters in letters for characters in word]
    return(all(letter_check))

#Problem 1: Sum of Integers.
def Problem_One():
    print("This is the first problem.") 
    n = int(input("Enter a positive integer: "))
    total = n * (n+1) / 2
    print("The sum of the first",n,"positive integers",total)

#Problem 2: Valid Word?
def Problem_Two():
    userWord = input('Enter a word to validate: ')
    with open('words.txt') as words_file:
        for line in words_file:
            if userWord == line.strip():
                print('{} is a valid word!\n'.format(userWord))
                return True
    print('{} is not a valid word.\n'.format(userWord))
    return False

#Problem 3: Can word be made from tiles?
def Problem_Three():
    print("This is the third problem.") #TODO Replace Me

#Problem 4: Find all words that can be made from tiles.
def Problem_Four():
    print("This is the fourth problem.") #TODO Replace Me

#Problem 5: NYT Spelling Bee Puzzle.
def Problem_Five():
    letters_of_the_day = Get_Letter_Set() # Letters from the Example
    center_letter = input('Please Enter your Center Character: ')
    letters_of_the_day += center_letter
    solved_words = []
    with open('words.txt') as words_file:
        for line in words_file:
            word = line.strip()
            if (len(word) >= 5) and (center_letter in word) and (Is_Letter_In_String(letters_of_the_day, word)):
                solved_words.append(word)
    if (len(solved_words) != 0):
        print('\nFound Words:')
        print(*solved_words, sep=', ')
    else:
        print('Words not found...')

#Problem 6: Most bingos?
def Problem_Six():
    print("This is the sixth problem.") #TODO Replace Me

def Reset():
    input("Press any key to continue.")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # used this to clear console instead of getting into os specific commands. If you know a better way feel free to implement it.

def Main():
    isRunning = True
    while isRunning:
        print("Welcome!")
        print("\n1: Sum of Integers"
            + "\n2: Valid Word?"
            + "\n3: Can word be made from tiles?"
            + "\n4: Find all words that can be made from tiles."
            + "\n5: NYT Spelling Bee Puzzle."
            + "\n6: Most bingos?"
            + "\n7: Exit Program.")
        selection = input("\nPlease enter the corresponding number for the program that you'd like to test: ")

        if int(selection) == 1:
            Problem_One()
        elif int(selection) == 2:
            Problem_Two()
        elif int(selection) == 3:
            Problem_Three()
        elif int(selection) == 4:
            Problem_Four()
        elif int(selection) == 5:
            Problem_Five()
        elif int(selection) == 6:
            Problem_Six()
        elif int(selection) == 7:
            isRunning = False
        else:
            print("Please enter a valid selection.")

        Reset()

Main()
