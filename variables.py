import math
# some testing
media1 = 10
media2 =10
media3 = 10
m = media1*1 + media2*2 + media3*3
mediaAnual = m/6
print(type(mediaAnual)) 
print(math.floor(mediaAnual))
#complex type (complex number in math)
print(type(1+2j))

#Function isintance([data],[(type1, type2, ...typen)]), which returns true or false on the type of datatype you think the data is.
print(isinstance(media1, str))