#created with curly brackets
#sets do not show duplicated values
planeta_anao = {'Plutão', 'Ceres','Eris', 'Haumea', 'Makemake'}

#to transform a list,tuple or dictionary into a set, use set()
astros_lista = ['Lua', 'Vênus', 'Sírius', 'Marte', 'Lua']
astros_set = set(astros_lista)

astros1 = {'Vênus', 'Sírius', 'Marte', 'Lua', 'Io'}
astros2 = {'Vênus', 'Sírius', 'Marte', 'Lua', 'Cometa de Halley'}
#Union of two or more sets: set1 | set2
print(astros1 | astros2)
#or with set1.union(set2)
print(astros1.union(astros2))

#Intersection of two or more sets: set1 & set2
#or with set1.intersection(set2)
print(astros1 & astros2)
print(astros1.intersection(astros2))

#Symmetric Difference, that is, the element that is not common to both sets, is represented as: set1 ^ set2
#or with set1.symmetric_difference(set2)
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

#to add an element in a set, use set.add()
astros1.add('Urano')
print(astros1)

#to remove an element in a set, use set.remove() or set.discard()
astros1.remove('Io')
print(astros1)

#to remove random element, use set.pop(), with no argument
astros1.pop()
print(astros1)

#to clear the entire set, use set.clear()
astros1.clear()
print(astros1)