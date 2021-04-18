"""
https://www.hackerrank.com/challenges/write-a-function/problem

Sample Input 0

1990
Sample Output 0

False
Explanation 0

1990 is not a multiple of 4 hence it's not a leap year.

"""


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 ==0:
        leap = True
    if year%100==0:
        leap = False
    if year%400==0:
        leap = True
    
    return leap

year = int(input())