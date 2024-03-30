#lambda (anonymous) functions
#lambda functions are functions that doesn't have names and can be used at the same time.
#syntax: lambda arguments : expression
square = lambda x: x**2         #square of a number

#to call the function, write () after the variable that it was assigned
for i in range(1,11):
    print(square(i))

#example to see if a number is even or not.
even = lambda x : x % 2 == 0
print(even(20))

#example conversion from fahrenheit to celsius
celsius = lambda f :  (f-32)*5/9
print(celsius(120))

#map() function: a function that applies functions
#syntax: map(function, iterable object). i.e. for each iterable object, a given function will be applied to it.

#example of doubling every element of a list using map()
list1 = [1,2,3,4,5,6,7,8,9,10]
mult = list(map(lambda x : 2*x,list1))      #it was converted to a list because it would not show otherwise on the terminal
print(mult)

#example trying to capitalize every string of a list
words = ['Python', 'is', 'a', 'programming', 'language']
cap = list(map(str.upper, words))           #instead of writing lambda x: x.upper(), we can just write str.upper
for i in cap:
    print(f'{i}', end=' ')

#filter() function: filter elements of a sequence
#Syntax: function(function, sequence)
#It works with Boolean types when extracting the elements of a sequence based on parameters of a function

def even_num(a):
    return a % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,13,16,17,18,19,20]
filter_function = list(filter(even_num, numbers))         #write the function name without parentheses
print(filter_function)

odd_num = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_num)

#reduce() function *it has to be imported from functools*: cummulative operations over elements of a sequence
#syntax: reduce(function, sequence, initial_value)
from functools import reduce

def mult(a,b):
    return a*b

num = [1,2,3,4,5,8,73,32]
total = reduce(mult, num)           #no need to write () in function
print(total)

total = reduce(lambda x, y: x**2 + y**2, num)
print(total)