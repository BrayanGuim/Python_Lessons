#A condition is made where it will be in looping if it reads it as True, but will stop when the statement be False
chiffre = 1

#'while' is used as the conditionals, you write a statement and if it is True, it will run the code, otherwise it will not
#It sees if it is true as many times as we want 
while (chiffre <= 2):
    print(chiffre)
    chiffre += 1

#'None' is used as a placeholder
nome = None
#To create an infinite sequence, just write True in the argument, as below
while True:
    print('Digite seu nome, ou x para parar: ', end='')
    nome = input()
    if (nome == 'x' or nome =='X'):
            break #break stops the 'while' loop
    print(f'Bem vindo {nome}!')
print('Até logo!')