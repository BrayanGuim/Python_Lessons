#we can access individual letters of string by string_name[i]
name = 'Brayan'
letter = name[3]
print(letter)

#we can split a string, making its words part of a list with the method string_name.split()
frase = 'Vamos aprender Python hoje.'
palavras = frase.split()
print(palavras)

'''
#we can find the position of a character by writing string_name.find(character)
email = input('Insira seu endereço de email: ')
arroba = email.find('@')
print(arroba)
#we are done slicing below to separate the user name from the after @'s
usuario = email[0:arroba]
dominio = email[arroba+1:] #arroba + 1 because I want the character after arroba
print(usuario)
print(dominio)
'''

#to use upper case, just write string_name.upper()
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.upper())
#to use lower case, just write string_name.lower()
print(objeto_celeste.lower())
#to capitalize just the first letter, use string_name.capitalize()
print(objeto_celeste.capitalize())
#to capitalize every word, use string_name.title()
print(objeto_celeste.title())

#to replace a substring, use string_name.replace(which word, by what word)
suplemento = 'cloreto de magnésio'
novo_suplemento = suplemento.replace('magnésio', 'powder')
print(suplemento)
print(novo_suplemento)

#to eliminate white spaces in the beginnin or end of a string, use string_name.lstrip(), string_name.rstrip(), string_name.strip(), where lstrip takes the left side, the rstrip the right side, and strip both sides.
frase = '           Ômega 3 é bom para a saúde!              '
print(frase)
print(frase.strip())

#we can align the string using string_name.rjust(# of characters to use with the word of the string)
fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20)) #right justify means there are in total 20 characters from the last letter of the string down to the left side
#to center the string, use string_name.center(#)
print(fruta.center(40))
#the same concept is used to justify on the left, but we can choose how is the blank space going to be filled with string_name.ljust(#, 'string')
print(fruta.ljust(20,'-'))
print(fruta.center(20,'-'))

#we can know if a string starts or end with a certain substring using string_name.startswith(substring) and string_name.endswith(substring), respectively [Boolean Type]
p = 'Bóson Treinamentos'
print(p.startswith('Bó'))
print(p.endswith('tos'))

#Docstring: parecido com comentários mas para documentar trechos do código, ''' ''''
#we can also assign it to a variable
texto = '''
Exemplo
'''
print(texto)