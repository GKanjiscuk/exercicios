#verifique se um número inteiro positivo é primo
num = int(input('Digite um número:'))
i = 1
divisores = [1]

while (i <= num):
        i += 1
        # print(f'Divisor atual: {i}')
        # print(f'Divisores armazenados: {divisores}')
        if(num % i == 0):
            divisores.append(i)

if(len(divisores) == 2):
      print(f'O número: {num}, é primo.')
      print(f'Divisores: {divisores}')
else:
      print(f'O número: {num}, não é primo.')
      print(f'Divisores: {divisores}')