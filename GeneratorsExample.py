## GENERATOR EXAMPLES

## Generate numbers from square
def gensquare(N):
	for i in range (N):
		yield i**2

for x in gensquares(10):
	print(x)

## Generate numbers from range
import random

random.randint(1,10)

## Generate lowest and highest numbers in range

def rand-num(low, high, n):

	for i in range(n):
		yield random.randint(low,high)

	for num in rand_num(1,10,25)
		print(num)

## User iter() string to convert to an iterator

s = 'Gametime'

s = iter(s)

print(next(s))

## Print everything from item in list

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
	print(item)

