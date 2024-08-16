n = int(input('Digite a posição que deseja saber o número da sequência de fibonacci: '))
i = 1
a, b = 1, 1
while (i != n):
    a, b = b, a + b
    i = i + 1
print(f'O número que pertence à {n}° posição da sequencia de fibonacci é: {a} ')
