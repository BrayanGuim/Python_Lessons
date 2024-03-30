import random
#start by importing the random method
n = random.randint(1, 50)
#syntax: random.randit(range from initial value, to final value)

print('Gerar cinco números aleatórios de 1 a 50: \n')
for i in range(5):
        n = random.randint(1, 50)
        print(f'Número gerado: {n}')
#A variable defined outside a loop is different from the same defined inside the loop

value = random.random() #Same as random.randit() but with float, and no argument
print(f'\nNúmero gerado: {round(value*10 , 3)}') #syntax: round(number, decimal places)

value = random.uniform(1,100)           #same as random() but you can specify the initial and final value
print(f'\nNúmero: {round(value, 2)}')

L=[2,6,7,34,76,32,7,8,9,12,10,5,3,53,33]
n= random.choice(L) #syntax: random.choice(name of a list)
print("Número escolhido: {0}".format(n))

n = random.sample(L, 3) #syntax: random.sample(name of the array, amount of numbers you want from the list)
print('Novos números escolhidos: {0}'.format(n))

print(f'Exibir a lista original: {L}')
print('Embaralhar a lista e exibi-la: ')
n = random.shuffle(L) #syntax: random.shuffle(name), serve para embaralhar lista
print(L)