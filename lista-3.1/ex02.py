valor = int(input('Digite o valor a ser pago: '))
pagamento = int(input('Digite o pagamento efetuado: '))
notas = [50, 20, 10, 5, 2, 1]
troco = pagamento - valor
trcCliente = []

for nota in notas:
    while troco >= nota:
        trcCliente.append(nota)
        troco = troco - nota

  
print(f'Troco: {trcCliente} ')

