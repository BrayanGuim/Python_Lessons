# you can force an error to occur by writing 'raise Error_name'
from math import sqrt

#we can create our own exceptions by writing: 'class NewErrorName(Exception):'
class NegativeNumberError(Exception):
    def __init__(self):
        pass            #pass means 'ignore and follow with the code straight ahead. It is useful to test the code without providing a code

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Type a positive number: '))
            if num < 0:
                raise NegativeNumberError
        except NegativeNumberError:
            print('Negative number inputted, try again.')
        else:
            print(f'The square root of {num} is {round(sqrt(num), 2)}')
            break
        finally:
            print('End.')