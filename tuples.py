#Tuples are immutable, kind of a sequence of constants, instead of a sequence of variables
#Syntax: tuple_name = (a1,a2,a3,...,aN)

halogène = ('F', 'Cl', 'Br', 'I', 'At')
gaz_noble = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
éléments = halogène + gaz_noble
t1 = (1,35,3,2,3,3,9,75,8,5,4,36,75,35)
#We can count the number of repetitions in a tuple using  tuple_name.count(value)
print(t1.count(100))

#functions not available for tuples: sort(), append(), pop(), reverse(), ...
#You can transform a tuple into a list and vice-versa using the list() and tuple() functions
groupe = list(halogène)
print(sorted(groupe))