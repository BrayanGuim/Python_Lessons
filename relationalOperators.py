#Boolean type, therefore, returns true or false
a= 2==2
b= 3==1
print(a, b)
# the "==" is basically like asking "are those two data equal to each other?"
c = 5!=5
print(c)
# the same concept applies to "!="
# key idea: two symbols means comparision (True or False)
z = 5
w = int(5)
print (z==w)
# below is some practice 
x = y = z = False
n1=n2=0
n1=int(input("Escreva o seu número: "))
n2=int(input('Escreva outro número aqui: '))

x = n1==n2
print("São enguais? ",x, '\n')
# the '\n' string refers to a line break (br)
y = n1!=n2
print("São diferentes? " + str(y))
# When concatenating, you can only concatenate strings, that is why I converted 'y' to a string.