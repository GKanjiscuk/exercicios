resposta = []
contador = 0
for num in range(18644, 33087):
    if '2' in str(num) and '7' not in str(num):
        resposta.append(num)
        contador += 1
print (f'{contador} números')
# print(f'Lista: {resposta}')