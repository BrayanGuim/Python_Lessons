#Exception: an object that represents an error in the process of the program
#Blocos: try ... except
#inside the 'try' statement, you put the section of the code which may give an error, and inside the 'except' you put the 'tratamento do erro'

def division(k,j):
    return round(k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Undefined input! Try again.')
    try:
        r = division(n1,n2)
    except ZeroDivisionError:
        print('Division by Zero! Try again.')
    except:
        print('An unknown error occurred!')
    else:  
        print(f'Resultado: {r}')
    finally:
        print(f'\nEnd of calculation.')
#the 'finally' statement shows a block of code that will run in all cases, giving error or not.
# if you don't write which error occurred, then the exception will apply to all errors
# to write multiple excepctions, write: except expt1,expt2, ...:
# else is used to show, if an error doesn't occur, then ...:
