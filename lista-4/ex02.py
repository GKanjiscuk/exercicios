from random import sample
numeros = sample(range(100), 20)
impares = []
pares = []

for k in numeros:
    if k % 2 == 0:
        pares.append(k)
    else:
        impares.append(k)

print(f'Números: {numeros}')
print(f'Ímpares: {impares}')
print(f'Pares: {pares}')