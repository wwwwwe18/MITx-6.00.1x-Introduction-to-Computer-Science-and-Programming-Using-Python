"""
Problem Set 1, Problem 2

Assume s is a string of lower case characters. Write a program that prints the
number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print:
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
num_count = 0
for n in range(0,len(s),1):
    if(s[n:n+3] == 'bob'):
        num_count = num_count + 1
print("Number of times bob occurs is: " + str(num_count))
