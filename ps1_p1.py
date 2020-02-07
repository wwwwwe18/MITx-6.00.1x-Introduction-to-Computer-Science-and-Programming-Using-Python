"""
Problem Set 1, Problem 1

Assume s is a string of lower case characters. Write a program that counts up
the number of vowels contained in the string s. Valid vowels are: 'a', 'e',
'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""

s = 'azcbobobegghakl'
num_count = 0
for n in range(0,len(s),1):
    if((s[n] == 'a') or (s[n] == 'e') or (s[n] == 'i') or (s[n] == 'o') or (s[n] == 'u')):
        num_count = num_count + 1
print("Number of vowels: " + str(num_count))