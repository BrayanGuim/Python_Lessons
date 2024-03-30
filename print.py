#Sintax: print(object, argument) <-- an argument is something after the comma
nome = 'Brayan Guimarães'
canal = 'Bóson Treinamentos'
print(canal,'-',nome)
#Example of arguments below:
print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha',  end="") #the argumento end='' means no line break (br)
print(' Continuo na mesma linha')

#Second example below:
nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome,idade) #the .format({1},{2}, ...{n}) is like JS arrays.

print(msg_formatada)

#Another example below:
nome = 'Brayan'
peso = 60.05
msg = f'Olá, meu nome é {nome} e peso {peso}kg' #f-string allows the direct implementation of a variable into a string.
print(msg)
#Its notation are f'string'
#another example of f'string' below:
a = 10
b  = 5
ans = f'The result of {a} plus {b} gives {a + b}' #You can insert expressions

print(ans)

#More utilities below:
valor = 154.0472648
print(f'O valor é {valor:.2f}') #The (object:function) means an order which the variable is given
#the '.2' states how many numbers do I want to see after the comma
#the 'f' after the number states that it is a floating number, and the result is a number rounded up, let's go to the next example now
nome = 'João'
idade = 47
print(f'Nome: {nome}\t Idade: {idade}') #the \t gives more spacing
