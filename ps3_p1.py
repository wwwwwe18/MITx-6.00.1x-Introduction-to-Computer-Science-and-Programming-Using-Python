"""
Problem Set 3, Problem 1

Please read the Hangman Introduction before starting this problem. We'll start 
by writing 3 simple functions that will help us easily code the Hangman problem. 
First, implement the function isWordGuessed that takes in two parameters - 
a string, secretWord, and a list of letters, lettersGuessed. This function 
returns a boolean - True if secretWord has been guessed (ie, all the letters of 
secretWord are in lettersGuessed) and False otherwise.

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
False
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    out_flag = 1
    
    for i in secretWord:
        if(i in lettersGuessed):
            out_flag *= 1
        else:
            out_flag = 0
    return(out_flag == 1)

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))