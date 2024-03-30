a = 10
b = 5
print(a/b)
# different from the simple division (/), the divisio with two bars (//) gives only the whole number output, with no floating number
print(a//b)
# the input("") function allows the user to type in whatever he wants
a = int(input("type your number here: "))
b = int(input("type your other number here: "))
# the reason I put the int([expression]) function up here was because it was concatenating the int instead of adding them
# I used the Casting, which is converting a data type to another data type, like in int(), str(), bool(), etc...
z = a + b
print(z)