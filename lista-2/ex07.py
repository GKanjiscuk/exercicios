#  1L ------ 3m²
# 18L ------ 54m² (1 lata de tinta = R$80,00)

area = int(input('Insira a área a ser pintada (m²): '))
if (area % 54 == 0):
    latas = area/54
elif (area % 54 > 0 ):
    latas = int(area/54) + 1
total = latas * 80
print(f'Latas de tinta necessárias: {latas}')
print(f'Total: R$ {total:.2f}')