"""
Problem Set 3, Problem 3

Next, implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters that 
are not in lettersGuessed.

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
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

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))