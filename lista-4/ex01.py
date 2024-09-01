import random
from random import sample
numeros = sample(range(100),10)
maior = menor = numeros[0]

for k in range(10):
    if numeros[k] > maior: maior = numeros[k]
    if numeros[k] < menor: menor = numeros[k]

print(f'vetor: {numeros}')
print(f'maior: {maior}')
print(f'menor: {menor}')