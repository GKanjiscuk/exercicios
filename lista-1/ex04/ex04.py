antigo_salario = int(input('Digite o valor do salário atual:'))
aumento = int(input('Digite o percentual de aumento (somente valor, sem %):'))

novo_salario = antigo_salario + (antigo_salario * aumento/100)

print('O antigo salário era', antigo_salario,'O novo salário com o aumento de', aumento, '% é de', novo_salario)