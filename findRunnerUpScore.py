"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.


"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    out = list(arr)
    out.sort()
    out = list(dict.fromkeys(out))
    print(out[-2])
