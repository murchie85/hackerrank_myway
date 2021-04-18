"""
https://www.hackerrank.com/challenges/the-minion-game/problem

Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.


I didn't like this problem set as the rule was insufficiently defined. Input is all variations on banana, not actually other words... I initially made a huge full proof solution which wasn't necessary.
"""



def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")

if __name__ == '__main__':