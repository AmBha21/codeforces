"""You are given a bracket sequence 𝑠
 of length 𝑛
, where 𝑛
 is even (divisible by two). The string 𝑠
 consists of 𝑛2
 opening brackets '(' and 𝑛2
 closing brackets ')'.

In one move, you can choose exactly one bracket and move it to the beginning of the string or to the end of the string (i.e. you choose some index 𝑖
, remove the 𝑖
-th character of 𝑠
 and insert it before or after all remaining characters of 𝑠
).

Your task is to find the minimum number of moves required to obtain regular bracket sequence from 𝑠
. It can be proved that the answer always exists under the given constraints.

Recall what the regular bracket sequence is:

"()" is regular bracket sequence;
if 𝑠
 is regular bracket sequence then "(" + 𝑠
 + ")" is regular bracket sequence;
if 𝑠
 and 𝑡
 are regular bracket sequences then 𝑠
 + 𝑡
 is regular bracket sequence.
For example, "()()", "(())()", "(())" and "()" are regular bracket sequences, but ")(", "()(" and ")))" are not.

You have to answer 𝑡
 independent test cases.

Input
The first line of the input contains one integer 𝑡
 (1≤𝑡≤2000
) — the number of test cases. Then 𝑡
 test cases follow.

The first line of the test case contains one integer 𝑛
 (2≤𝑛≤50
) — the length of 𝑠
. It is guaranteed that 𝑛
 is even. The second line of the test case containg the string 𝑠
 consisting of 𝑛2
 opening and 𝑛2
 closing brackets.

Output
For each test case, print the answer — the minimum number of moves required to obtain regular bracket sequence from 𝑠
. It can be proved that the answer always exists under the given constraints."""

tests = int(input())

for i in range(tests):
    n = input()
    s = input()
    counter = 0
    for i in range(len(s)):
        if s[i] == '(':
            counter += 1
        elif s[i] == ')' and counter > 0:
            counter -= 1
        else:
            counter = 0
    print(counter)