resposta = []
for i in range(1067, 3627):
    if (i % 2 == 0 and i % 7 == 0):
        resposta.append(i)

print(resposta)
print()
print(f'{len(resposta)} números')