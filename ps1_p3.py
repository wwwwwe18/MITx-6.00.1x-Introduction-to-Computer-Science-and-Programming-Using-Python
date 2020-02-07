"""
Problem Set 1, Problem 3

Assume s is a string of lower case characters. Write a program that prints the
longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print:
Longest substring in alphabetical order is: abc
"""

s = 'azcbobobegghakl'
#s = 'jurzwysgsbx'
#s = 'zyxwvutsrqponmlkjihgfedcba'

import string

alpha_index = []
alpha_out = []
alpha_out_len = []

for i in range(0,len(s)):
    alpha_index.append(0)
    alpha_out.append('')
    alpha_out_len.append(0)
    alpha_index[i] = string.ascii_lowercase.index(s[i])
    
alpha_str = 0
i = 0
while(i < len(s)-1):
    count_temp = i
    while(alpha_index[count_temp] <= alpha_index[count_temp+1]):
        count_temp = count_temp + 1
        if(count_temp == len(s) - 1):
            break
    count_end = count_temp + 1
    alpha_out[alpha_str] = s[i:count_end]
    alpha_out_len[alpha_str] = count_end - i
    alpha_str = alpha_str + 1
    i = count_end

for i in alpha_out:
    if(len(i) == max(alpha_out_len)):
        print("Longest substring in alphabetical order is: " + i)
        break