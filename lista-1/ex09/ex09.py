dias = int(input('Insira a quantidade de dias em que o carro foi alugado: '))

km = float(input('Insira quantos quilômetros o carro percorreu durante o período alugado'))

total = (dias * 60) + (km * 0.15)

print('O preço total a se pagar é de:', total)