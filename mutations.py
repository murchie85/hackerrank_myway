"""
https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
Sample Output

abrackdabra


"""


def mutate_string(string, position, character):
	s_new = str(string[:position]) + str(character) + str(string[position+1:])
	return(s_new)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)