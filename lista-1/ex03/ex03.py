dias = int(input('Dias: '))
h = int(input('Horas: '))
min = int(input('Minutos: '))
secs = int(input('Segundos: '))

resultado = (dias * 24*60*60) + (h*60*60) + (min*60) + secs

print(dias, 'dias,', h, 'horas,', min, 'minutos,', 'e', secs, 'segundos em segundos é: ',  resultado, 'segundos')