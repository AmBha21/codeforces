"""Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.

Input
The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

Output
If Vasya managed to say hello, print "YES", otherwise print "NO"."""

# Misunderstood the question, thought it was a substring problem
# from collections import Counter

# s = input()
# h_dict  = dict(Counter('hello'))
# for i in s:
#     if i in h_dict and h_dict[i] >= 1:
#         h_dict[i] -= 1

# output = True
# for i in h_dict.values():
#     if i != 0:
#         output = False
#         print('NO')
#         break

# if output:
#     print('YES')

counter = 0
s = input()
for i in s:
    if i == 'h' and counter == 0:
        counter += 1
    elif i == 'e' and counter == 1:
        counter += 1
    elif i == 'l' and counter == 2:
        counter += 1
    elif i == 'l' and counter == 3:
        counter += 1
    elif i == 'o' and counter == 4:
        counter += 1
if counter == 5:
    print('YES')
else:
    print('NO')