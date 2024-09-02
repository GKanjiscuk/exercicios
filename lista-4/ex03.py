from random import sample
from random import randint
num1 = []
num2 = []
num3 = []
for k in range(10):
    x = randint(1,100)
    num1.append(x)
    num3.append(x)
    x = randint(1,100)
    num2.append(x)
    num3.append(x)

print(f'Vetor 1: {num1}')
print(f'Vetor 2: {num2}')
print(f'Vetor 3: {num3}')