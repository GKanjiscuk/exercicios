l1 = int(input('Digite algum lado do triangulo (lado 1):'))
l2 = int(input('Digite outro lado do triangulo (lado 2):'))
l3 = int(input('Digite o último lado do triangulo (lado 3):'))

if (l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2):
    print('Os lados indicados não podem formar um triângulo')
elif(l1 == l2 == l3):
    print('Equilátero')
elif (l1== l2 or l2 == l3 or l3 == l1):
    print('Isósceles')
else: 
    print ('Escaleno')