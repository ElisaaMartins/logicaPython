''' 
Problema 1 - Valor por hora
Escreva um programa que retorna o valor hora de um funcionário
com base no seu salário mensal e horas trabalhadas por mês.
'''

salario_mensal = input("Qual seu salário mensal? ") #input retorna texto
horas_mes = input("Quantas horas trabalha por mês? ")

valor_hora = float(salario_mensal) / float(horas_mes) #tem que converter

print(valor_hora)