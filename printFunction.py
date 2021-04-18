"""
https://www.hackerrank.com/challenges/python-print/problem


Output Format

Print the list of integers from  through  as a string, without spaces.

Sample Input 0

3
Sample Output 0

123

"""


if __name__ == '__main__':
    n = int(input())
    myarray = []
    if n in range(1,151):
        for x in range(1,n+1):
            print(x,end="")
