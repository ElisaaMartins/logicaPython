# Problema - Gastos totais com pagamento de salários.
# Dado uma lista de salários, calcule o total pago a todos os funcionários

'''
salarios = [1000, 200, 300]
salarios_total = salarios[0] + salarios[1] + salarios[2]

print(salarios_total)
'''

salarios = [1000, 200, 300]
salarios_total = 0

for salario in salarios:
    salarios_total = salarios_total + salario

print(salarios_total)