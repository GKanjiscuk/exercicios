print('Calculadora de Máximo Divisor Comum (MDC)')
print ('Informe dois números que deseja saber o Máximo Divisor Comum ')
a = n1 = int(input('N°1: '))
b = n2 = int(input('N°2: '))

while (a % b != 0):
    a, b = b, (a % b)
    # print(f'a: {a}  b:{b}')
print(f'O máximo divisor comum entre {n1} e {n2} = é {b}')
