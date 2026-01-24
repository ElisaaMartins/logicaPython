# Problema:
# Crie um programa que recebe dois valores e exibe qual é o maior entre eles.

valor1 = float(input("digite o valor 1 "))
valor2 = float(input("digite o valor 2 "))

if valor1 > valor2:
    print("valor 1 é maior")
elif valor2 > valor1:
    print("valor 2 é maior")
else:
    print("os valores são os mesmos")