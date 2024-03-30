# Simple conditional

'''media = input('Média mensal: ')

if (media >= 7): 
    print('Você foi aprovado!!')
print('Você reprovou!' + '\n' + '\n')'''

#There is no need for "else" in this simple conditional,  the only thing needed is that the "else line" be in another indentation
#Now, doing the "condicional composto", we get to use the "else" statement:
n1=n2=0.0
media2 = 0.0

n1 = float(input('digite a sua primeira nota aqui: '))
n2= float(input('digite a sua segunda nota aqui: '))
media2=(n1+n2)/2
#You cannot break lines (br) when writing a conditional
#Condicional Encadeado: use of "elif", to express another sub-condition
#*ELIF CAN BE USED INFINITE TIMES! 
if (media2>=7):
    print('You aced it! Well done! Sua média foi: '+ str(media2))
elif (media2>=5):
    print('Você está de recuperação! Sua nota final foi: ' + str(media2))
else: 
    print("You've failed it bro! Try another time, sua nota final é: " + str(media2))
