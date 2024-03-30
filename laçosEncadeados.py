#definition: loop inside a loop
for x in range(1,6):
    print(f"\nRodada: {x}")
    for y in range(5,0,-1):
        print(f"Valor: {y}")
#internal looping runs itself 5 times for each external looping
print('\nLoop End')

import random
for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):          #range(n) runs n times
        number = random.randint(1,100)
        print(f'Valor: {number}')
#syntax of import random: random.[function](initial value, end value)