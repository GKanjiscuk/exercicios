preço = float(input('Informe o valor da mercadoria:'))
desconto = float(input('Informe o percentual de desconto (somente valor):'))

valor_desconto = preço * desconto/100
total  = preço - (valor_desconto)


print('Desconto de:', valor_desconto, 'reais. O preço total a se pagar é de:', total, 'reais' )