cigarros = int(input('Informe a quantidade de cigarros fumados por dia: '))
anos = int(input('Informe há quantos anos possui este hábito: '))

# um dia possui 1440 minutos
# logo, um dia = 144 cigarros 
total_cigarros = cigarros*365*anos
tempo_perdido = total_cigarros / 144 

print (f'Você perdeu {tempo_perdido:.1f} dias de vida')

#:.1f: É um formato numérico. O ponto (.) indica um separador decimal e o 1f significa que queremos exibir apenas uma casa decimal após o ponto.
