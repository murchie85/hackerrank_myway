"""
https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Sample Input

qA2
Sample Output

True
True
True
True
True



KNOWLEDGE


validators include 

str.isalnum()
str.isalpha()
str.isdigit()
str.islower()
str.isupper()

"""

def iterateString(string):
	
	alnum = "False"
	for l in string:
		if(l.isalnum() == True):
			alnum = "True"
			break

	isalpha = "False"
	for l in string:
		if(l.isalpha() == True):
			isalpha = "True"
			break

	isdigit = "False"
	for l in string:
		if(l.isdigit() == True):
			isdigit = "True"
			break

	islower = "False"
	for l in string:
		if(l.islower() == True):
			islower = "True"
			break

	isupper = "False"
	for l in string:
		if(l.isupper() == True):
			isupper = "True"
			break
	return(alnum,isalpha,isdigit,islower,isupper)
if __name__ == '__main__':
    s = input()
    out = iterateString(s)
    for item in out: print(item)