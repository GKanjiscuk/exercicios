distancia = int(input('Informe a distancia a ser percorrida em quilômetros: '))
velocidade = int(input('Informe a velocidade média esperada para a viagem em km/h: '))

tempo = float(distancia/velocidade)

mins = tempo * 60

print('A viagem levará', tempo, 'horas ou', mins, 'minutos.')