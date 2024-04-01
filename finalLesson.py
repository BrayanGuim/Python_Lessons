#(1)Change values between two variables
var1 = 12
var2 = 31

var2, var1 = var1, var2
print(f'var1: {var1}; var2: {var2}')

#(2)Ternary Operator: Compact conditional statements
less_than = var1 if var1 < var2 else var2 #return var1 if var1 < var2; else return var2
print(f'Lowest value: {less_than}')

#(3)Generators: Same as list comprehension but with parentheses (consume less memory).
values = [1, 3, 5, 7, 9, 11, 13, 15]
squares = (item**2 for item in values)
print(list(squares))

#(4)Enumerate function
drinks = ['Coffee', 'Tea', 'Water', 'Juice', 'Soda']
for i, item in enumerate(drinks):
    print(f'Index: {i + 1}; Items: {item}')

temperatures = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperatures):
    if t < 0:
        print(f'\nThe temperature on {i} is negative, with {t}°C')

#(5) with
try:
    a = open('GitProjects/PythonProjects/pyLessons/functions.py', 'r')
    print(a.read())
except IOError:
    print('Impossible to read the file')
else:
    a.close()

with open('GitProjects/PythonProjects/pyLessons/file.txt', 'r') as a:
    for line in a:
        print(line)