# MITx-6.00.1x-Introduction-to-Computer-Science-and-Programming-Using-Python

# Problem Set 1
Problem 1
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5

Problem 2
Assume s is a string of lower case characters. Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print:
Number of times bob occurs is: 2

Problem 3
Assume s is a string of lower case characters. Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
Longest substring in alphabetical order is: abc

# Problem Set 2

# Problem Set 3
Problem 1 - Is the Word Guessed
Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
False

Problem 2 - Getting the User's Guess
Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'

When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of __ with _ _ ) This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

Problem 3 - Printing Out all Available Letters
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

import string
print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz

Problem 4 - The Game
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).
