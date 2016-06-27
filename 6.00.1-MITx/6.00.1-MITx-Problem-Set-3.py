# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord: 
        if letter not in lettersGuessed:
            return False
            break                         # return False as soon as a letter is not present in the guess list
    return True                           # return True otherwise


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordGuessedList = []
    wordGuessed = ''
    for letter in secretWord:
        # if letter is not guessed, use the dash
        if letter not in lettersGuessed: 
            wordGuessedList.append(' _ ')
        
        # if it was already guessed and if occurs more than once:     
        elif letter in lettersGuessed:
            wordGuessedList.append(letter) 
    
    # merge the list into string
    for letter in wordGuessedList: 
           wordGuessed += letter
    return wordGuessed


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ''
    for char in all_letters: 
        if char not in lettersGuessed:
            available_letters += char
            
    return available_letters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 8
    lettersGuessed = []
    guessed_word = ''

    print('Welcome to the game, Hangman!' + '\n' + 
    'I\'m thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    
    # while there are guesses left to be made
    while mistakesMade > 0:
        print('----------')

        # if the word was guessed, end the game
        if isWordGuessed(secretWord,lettersGuessed) :
            return ('Congratulations, you won!')
            break 
            
        print ('You have ' + str(guesses) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(lettersGuessed))
        guessed_letter = raw_input('Please guess a letter: ').lower()
        
        # if the letter was not guessed previously, added in the guessed list
        # and deducted the number of guesses by one
        if guessed_letter not in lettersGuessed:
            lettersGuessed.append(guessed_letter)
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
           
            if guessed_letter in secretWord and guessed_letter != '':                                
                print ('Good guess: ' + guessed_word)
            else: 
                print ('Oops! That letter is not in my word: ' + guessed_word)
                mistakesMade -= 1
            
        # if the letter was already guessed, do not take into account the guess
        else: 
            print ('Oops! You\'ve already guessed that letter: ' + guessed_word)
        # if there is no guesses left, end the game
        
    if isWordGuessed(secretWord,lettersGuessed) == False and mistakesMade == 0:
        print('----------')
        print ('Sorry, you ran out of guesses. The word was ' + secretWord +'.')
          





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
