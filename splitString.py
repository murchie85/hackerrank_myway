"""

https://www.hackerrank.com/challenges/python-string-split-and-join/problem

Sample Input

this is a string   
Sample Output

this-is-a-string
"""

def split_and_join(line):
    line = str(line) # convert to string
    splitted = line.split(" ")
    splitted = "-".join(splitted)
    return(splitted)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)