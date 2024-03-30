# the return statement stores the expression back to the function in a way that it can be used outside its function.
def mult(a,b):
    return a*b

a = 5
b = 8
c = mult(a,b)
print(f'O produto de {a} e {b} é {c}')

#you can assign values to a variable inside the argument of a function
def count(num = 11, character = '+'):
    for i in range(1,num): 
        print(character)

#you can reassign each variable inside the argument outside the function
if __name__ == '__main__' :
    count(num=8, character='@')

#example:
x = 5
y = 6
z = 3
# if the user types the value of c, the it will return a sum, otherwise, it will return a multiplication.
def sum_mult(a,b,c = 0):
    if c == 0:
        return a*b
    else:
        return a + b + c

if __name__ == '__main__':
    res = sum_mult(x,y,z)
    print(res)