#store data in key:value pairs.
#key is a string; value is the data associated with that string.
#to add more key-value pairs, a comma is needed by the end of each one.
element = {
    'Z':3, 
    'name': 'Lítio',
    'group': 'Metais Alcalinos',
    'density': 0.534
}
print(len(element))
print(element['group'])

#to change a value, type using the syntax dic_name[key] = new_value
element['group'] = 'Alcalinos'
print(element)

#to add a key and value, use the same syntax: dic_name[new_key] = new_value
element['period'] = 1
print(len(element))

#use del before the dic_name[key] to delete it
del element['period']
print(element)

#to delete the entire key-values , write dic_name.clear()
element.clear()
print(element)

#to delete the entire dictionary, use del dic_name
del element

#to see every item of dictionary, use dic_name.items()
#to see only the keys, use dic_name.keys()
#to see only the values, use dic_name.values()
print(element.items())
for i in element.items():
    print(i)

#we can assign two variables to a tuple.
for i, j in element.items():
    print(f'{i}: {j}')