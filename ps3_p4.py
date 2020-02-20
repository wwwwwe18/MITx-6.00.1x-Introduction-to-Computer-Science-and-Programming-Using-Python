"""
Problem Set 3, Problem 4

Now you will implement the function hangman, which takes one parameter - the 
secretWord the user is to guess. This starts up an interactive game of Hangman 
between the user and the computer. Be sure you take advantage of the three 
helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.

There are four important pieces of information you may wish to store:

1. secretWord: The word to guess.

2. lettersGuessed: The letters that have been guessed so far.

3. mistakesMade: The number of incorrect guesses made so far.

4. availableLetters: The letters that may still be guessed. Every time a player 
guesses a letter, the guessed letter must be removed from availableLetters 
(and if they guess a letter that is not in availableLetters, you should print a 
message telling them they've already guessed that - so try again!).

Winning info:

Loading word list from file...
55900 words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is 4 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ a_ _
------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! You've already guessed that letter: _ a_ _
------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: s
Oops! That letter is not in my word: _ a_ _
------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: t
Good guess: ta_ t
------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqruvwxyz
Please guess a letter: r
Oops! That letter is not in my word: ta_ t
------------
You have 6 guesses left.
Available letters: bcdefghijklmnopquvwxyz
Please guess a letter: m
Oops! That letter is not in my word: ta_ t
------------
You have 5 guesses left.
Available letters: bcdefghijklnopquvwxyz
Please guess a letter: c
Good guess: tact
------------
Congratulations, you won!

Losing info:

Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
-----------
You have 8 guesses left.
Available Letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! That letter is not in my word: _ _ _ _
-----------
You have 7 guesses left.
Available Letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: b
Oops! That letter is not in my word: _ _ _ _
-----------
You have 6 guesses left.
Available Letters: cdefghijklmnopqrstuvwxyz
Please guess a letter: c
Oops! That letter is not in my word: _ _ _ _
-----------
You have 5 guesses left.
Available Letters: defghijklmnopqrstuvwxyz
Please guess a letter: d
Oops! That letter is not in my word: _ _ _ _
-----------
You have 4 guesses left.
Available Letters: efghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: e_ _ e
-----------
You have 4 guesses left.
Available Letters: fghijklmnopqrstuvwxyz
Please guess a letter: f
Oops! That letter is not in my word: e_ _ e
-----------
You have 3 guesses left.
Available Letters: ghijklmnopqrstuvwxyz
Please guess a letter: g
Oops! That letter is not in my word: e_ _ e
-----------
You have 2 guesses left.
Available Letters: hijklmnopqrstuvwxyz
Please guess a letter: h
Oops! That letter is not in my word: e_ _ e
-----------
You have 1 guesses left.
Available Letters: ijklmnopqrstuvwxyz
Please guess a letter: i
Oops! That letter is not in my word: e_ _ e
-----------
Sorry, you ran out of guesses. The word was else.
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    list_out = list(string.ascii_lowercase)
    list_tmp = list_out.copy()
    str_out = "" 
    
    for i in list_tmp:
        if(i in lettersGuessed):
            list_out.remove(i)
    for i in list_out:
        str_out += i

    return str_out

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
    secretWord_len = len(secretWord)
    secretWord_list = list(secretWord)
    
    lettersGuessed = "_ "*(secretWord_len-1)+"_"
    lettersGuessed_list = list(lettersGuessed)
    
    import string
    availableLetters_org = string.ascii_lowercase
    availableLetters_list = list(availableLetters_org)
    availableLetters_list_tmp = availableLetters_list.copy()
    availableLetters = string.ascii_lowercase
    
    mistakesMade = 0
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(secretWord_len)+" letters long.")
    print("-----------")
    
    while((mistakesMade < 8)and(secretWord_list != [])):
        print("You have "+str(8-mistakesMade)+" guesses left.")
        print("Available Letters: "+availableLetters)
        user_guess = input("Please guess a letter: ")
        if(user_guess in secretWord):
            if(user_guess in availableLetters):
                # Update user_guess in lettersGuessed
                for i in range(len(secretWord)):
                    if(secretWord[i] == user_guess):
                        lettersGuessed_list[i*2] = secretWord[i]
                        lettersGuessed = ""
                for i in lettersGuessed_list:
                    lettersGuessed += i
            
                # Remove user_guess from secretWord_list
                for i in range(len(secretWord_list)):
                    if(user_guess in secretWord_list):
                        secretWord_list.remove(user_guess)
            
                # Remove user_guess from availableLetters
                if(user_guess in availableLetters_list_tmp):
                    availableLetters_list.remove(user_guess)
                availableLetters = ""
                for i in availableLetters_list:
                    availableLetters += i
                
                print("Good guess: "+lettersGuessed)
            else:
                print("Oops! You've already guessed that letter: "+lettersGuessed)
        else:
            if(user_guess in availableLetters):
                # Remove user_guess from availableLetters
                if(user_guess in availableLetters_list_tmp):
                    availableLetters_list.remove(user_guess)
                availableLetters = ""
                for i in availableLetters_list:
                    availableLetters += i
                print("Oops! That letter is not in my word: "+lettersGuessed)
                mistakesMade += 1
            else:
                print("Oops! You've already guessed that letter: "+lettersGuessed)
        print("-----------")

    if(mistakesMade < 8):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")

secretWord = 'tact' 
hangman(secretWord)