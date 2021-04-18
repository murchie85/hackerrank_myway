"""
https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.



# alternate options

# USING STARTSWITH 

def count_substringBest(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

# USING SLICE
def count_substringUsingSlice(string, sub_string):
	count = 0
	for letter in range(0,len(string)):
		if(string[slice(letter,letter+len(sub_string,1)] == sub_string):
			count+=1
	return(count)


"""





def count_substring(string, sub_string):
    count = 0
    for letter in range(len(string)):
        if(string[letter:letter+len(sub_string)] == sub_string):
            count+=1
    return(count)




if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)