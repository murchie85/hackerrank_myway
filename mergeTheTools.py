"""
Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD
Explanation

Split  into  equal parts of length . Convert each  to  by removing any subsequent occurrences of non-distinct characters in :

Print each  on a new line.

"""


def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    if(n >=1 and n <=10**4 + 1):
        a = int(n/k)
        printArray = []
        for x in range(0,a):
            subArray = []
            for y in range(x*k,(x*k)+k):
                subArray.append(string[y])
                
            subArray = list(dict.fromkeys(subArray))
            printArray.append(subArray)
        
        for item in printArray:
            printElement = ""
            for element in item:
                printElement += str(element)
            print(printElement)
                
        

if __name__ == '__main__':