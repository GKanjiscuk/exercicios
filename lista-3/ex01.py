nota = float(input('Informe uma nota: '))
while (nota > 10 or nota < 0):
    print('Nota inválida!! Informe uma nota entre 0 e 10')
    nota = float(input('Informe uma nota: '))
if(nota >= 0 and nota <= 10):
    print('Nota registrada')
