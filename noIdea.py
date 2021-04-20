"""
https://www.hackerrank.com/challenges/no-idea/problem

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT


arrayLen, setLen = map(int, input().split())
array            = list(map(int, input().split()))
setA             = list(map(int, input().split()))
setB             = list(map(int, input().split()))



happiness = 0
for number in array:
	if number in setA:
		happiness +=1
	if number in setB:
		happiness -=1

print(happiness)


sum([(i in setA) - (i in setB) for i in array])


print(sum([(i in setA) - (i in setB) for i in array]))