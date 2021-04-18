"""

https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

Sample Input 0

3
2
Sample Output 0

5
1
6


"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a >= 1 and a <= 10**10:
        if b>=1 and b<= 10**10:
            print(a+b)
            print(a-b)
            print(a*b)
