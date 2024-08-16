n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))
n3 = float(input('Insira um último número: '))

if (n1>=n2 and n1>=n3):
    maior = n1
elif (n2>=n3):
    maior = n2
else:
    maior = n3

print(f'{maior} é o maior numero')