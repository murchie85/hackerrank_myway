"""
https://www.hackerrank.com/challenges/python-loops/problem

Sample Input 0

5
Sample Output 0

0
1
4
9
16


"""


if __name__ == '__main__':
    n = int(input())
    for x in range(0,n):
        if x >= 0 and x<=20:
            print(x**2)


