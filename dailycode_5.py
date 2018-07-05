"""
This problem was asked by Jane Street.
cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:
def cons(a, b):
    return lambda f : f(a, b)
Implement car and cdr.
https://dailycodingproblem.com/
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def fa(a, b):
		return a
	return pair(fa)

def cdr(pair):
	def fd(a,b):
		return b
	return pair(fd)

if __name__ == '__main__':
	# Read input of two numbers, separated by commas
	a = 5
	b = 4
	#print(cons(a,b))
	print(car(cons(a, b)))
	print(cdr(cons(a, b)))