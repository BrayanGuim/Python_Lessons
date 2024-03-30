#list is also called arrays and matrices
#a list represents a sequence of values. Syntax: variable = [v1,v2,v3,...,vN]
n1 = [2,5,7,9,11,13]
n2=[1,3,4,6,8,10,12]

value = n1 + n2

#to see individual elements: variable[i], but to see the last value, type negative numbers starting with -1
print(value[-2])
#you can change each specific value: variable[i] = j
value[0] = 2
print(value)
#to show only a range of elements, write: variable[i:j]
print(value[-1:])
#to know how many elements are there on the list, use function len(list_name)
print(len(value))
#to sort the values from the lesser value to a higher number, use function sorted(list_name)
print(sorted(value))
#to show from greater to lesser, use sorted(list_name, reverse = True)
print(sorted(value, reverse=True))
#to sum all the values, use sum(list_name)
print(sum(value))
#to find either min or max value, use min(list_name) and max(list_name), respectively
print(max(value))
print(min(value))
#to add an element to the end of a list, use list_name.append(i)
value.append(50)
print(value)
#to remove last element from the list, use list_name.pop(), or list_name.pop(i) to remove a specific element
value.pop()
print(value)
#to insert a new element in a specific place, use list_name.insert(i, value)
value.insert(4,23)
print(value)
#to check if an element is inside the list, type 'number in list_name', it has a boolean type
print(12 in value,'\n')

#putting into practice below:
planets = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', "Urano", 'Neturno']
for planet in planets:
    print(planet)