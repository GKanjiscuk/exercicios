num = int(input('Digite um número: '))
i = 0
a, b, c = 1, 2, 3
while (i != num and i < num):
    i = a * b * c
    if(i<num):
        a, b, c = a+1, b+1, c+1
    
if(i==num):
    print(f'O número {num} é triangular ({a}*{b}*{c}={num})')
elif(i!=num):
    print('O número não é triangular')

