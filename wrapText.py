"""
https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


solution using textwrap 


import textwrap
s = input()
w = int(input())
l = " ".join(textwrap.wrap(s,w))
print(textwrap.fill(l,w))


"""



import textwrap

def wrap(string, max_width):
	printBlock = ""
	letterCount = 0
	for letter in string:
		letterCount +=1
		printBlock += letter
		if(letterCount == max_width):
			letterCount = 0
			printBlock += "\n"
	return(printBlock)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)