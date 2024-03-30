#syntax:"for 'item'  in 'sequence': instruções executadas para cada item."
# item = nome da variavel; sequence = vai possuir itens que serão todos executados
'''list = [1024,512,256,128,64,32,16,8,4,2,1,1/2,1/4,1/8,1/16,1/32,1/64,1/128,1/256,1/512,1/1024] 
#sintax de array: var = [a1,a2,a3,...an]  
#read: para cada item dentro da lista, ...; it can be item, letter, etc
    print(letter)'''
for number in range(0, 10):
#the range function is used here to show a list of numbers without creating a variable
#syntax: range(a0,aN), where a0 = initial value and aN= final value
    if (number == 1):
        print('hi')
    elif (number == 2):
        print('how are you?')
    elif (number == 3):
        print("i'm fine, thanks")
motRusse = "давай"
for letter in motRusse:
    if (letter ==  'д'):
        print('d', end='')
    elif (letter == "а"):
        print('a', end='')
    elif (letter == "в"):
        print('v', end='')
    elif (letter == 'a'):
        print('a', end='')
    else:
        print('y') 
print('давай')

nome = input('Insira o seu nome: ')
for x in range(10): # x means an unknown quantity of times, which is specified by range(10)
    print(f'{x + 1} {nome}') #{x + 1} means an adding of one for each 'nome', just like a list, beginning with 1 instead of 0

#range(valor_inicial, valor_final, incremento)
for x in range(2,20,2):
        print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Diamante', 'Safira', 'Turmalina')
for item in pedras:
    if (item == "Quartzo"):
        continue
    else:
        print(item)
# the 'continue' code is like break but does not stop the whole looping