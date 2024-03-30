#breaking a big problem into smaller ones, in a way that, in solving the smaller problems, they come together and make part of the solution of the bigger problem.
#factorial: if num = 0 and num = 1, then its factorial will be 1;  --->(base-case)
# else, factorial(num) = n * factorial(num-1)       --->(recursive case)
#example: 4! = 4 * factorial(3) => 4 * 3 * factorial(2) => 4 * 3 * 2 * factorial(1) = 4 * 3 * 2 * 1
#note that the function is calling itself multiple times before it reaches its base-case

def factorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num*factorial (num - 1)

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Type a number: '))
            if num >= 0:
                print(f'The factorial of the number {num} is equal to {factorial(num)}')
                break
            else:
                raise ArithmeticError
        except ArithmeticError:
            print('Negative integer typed. Try again.')
        except RecursionError:
            print('Number too big, try a smaller one')
        except ValueError:
            print('Undefined value, try again.')
        finally:
            print('End.')