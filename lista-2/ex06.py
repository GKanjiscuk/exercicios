valorHora = float(input('Insira o valor recebido por hora trabalhada: '))
horasTrabalhadas = int(input('Horas trabalhadas: '))

salBruto = valorHora * horasTrabalhadas
inss = 8*salBruto/100
IR = 11*salBruto/100
sindicato = 5*salBruto/100

totalDescontos = (inss + IR + sindicato) * -1
salLiquido = salBruto - inss - IR - sindicato

print(f"Salário bruto: R$ {salBruto:.2f}")
print("Descontos: ")
print(f" - INSS: R$ {inss:.2f}")
print(f" - Imposto de Renda: R$ {IR:.2f}")
print(f" - Sindicato: R$ {sindicato:.2f}")
print(f"Total de descontos: R$ {totalDescontos}")
print(f"Salário Líquido: R$ {salLiquido:.2f}")