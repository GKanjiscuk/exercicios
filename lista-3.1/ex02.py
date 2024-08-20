valor = int(input('Digite o valor a ser pago: '))
pagamento = int(input('Digite o pagamento efetuado: '))
notas = [50, 20, 10, 5, 2, 1]
troco = pagamento - valor
trcCliente = {}

for nota in notas:
    quantidade = 0
    while troco >= nota:
        troco = troco - nota
        quantidade += 1
        if (quantidade > 0):
            trcCliente[nota] = quantidade

print('Troco:')
for nota, quantidade in trcCliente.items():
    print(f'{quantidade} nota(s) de R$ {nota}')