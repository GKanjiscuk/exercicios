
while True:    
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    soma = n1 + n2
    print('A soma dos número é:', soma)
    print('Digite y para continuar executando e n para sair')
    continuar = input('Deseja continuar ?')
    continuar = continuar.lower()
    if continuar == 'n':
        print('Fim do programa')
        break
    
