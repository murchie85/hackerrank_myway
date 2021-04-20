"""
https://www.hackerrank.com/challenges/designer-door-mat/problem


Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""


N,M = map(int,input().split())
token = '.|.'


# Get the mid point of vertical and horizontal 
verticalCenter  = int(N/2 + 0.5) - 1
horizontalCenter = int(M/2 + 0.5)

print(verticalCenter)
print(horizontalCenter)


# First start with top half 
# The trick is to realise the token is equal to 1 * line number
tokenCount = 1;

for toprow in range(verticalCenter):
	rowBuffer   = ""
	tokenLen    = 3 * tokenCount


	dashLen = int((M - tokenLen)/2)

	# build a print string( row buffer)
	for i in range(dashLen):
		rowBuffer+='-'

	for i in range(tokenCount):
		rowBuffer+=token

	for i in range(dashLen):
		rowBuffer+='-'

	print(rowBuffer) 
	if(toprow < verticalCenter - 1	): tokenCount += 2




rowBuffer = ""
dashLen = int((M - len('WELCOME'))/2 )
for i in range(dashLen) : rowBuffer+='-'
rowBuffer+='WELCOME'
for i in range(dashLen) : rowBuffer+='-'


print(rowBuffer)



for bottomRow in range(verticalCenter):
	rowBuffer   = ""
	tokenLen    = 3 * tokenCount


	dashLen = int((M - tokenLen)/2)

	for i in range(dashLen):
		rowBuffer+='-'

	for i in range(tokenCount):
		rowBuffer+=token

	for i in range(dashLen):
		rowBuffer+='-'

	print(rowBuffer) 
	tokenCount -= 2	

