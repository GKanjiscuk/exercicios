num = int(input('Digite um numero: '))
for i in range(2,num):
    while (num % i == 0):
        print(i)
        num = num/i