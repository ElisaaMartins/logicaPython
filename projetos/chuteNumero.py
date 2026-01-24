# Projet 2 - Chute o número

'''
Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 10 e permita
que o usuário chute números até acertar o valor gerado.

O programa deve informar se o chute foi maior, menor ou igual ao valor aleatório
gerado no início.
'''


import random

valor_aleatorio = random.randint(1, 100)
acertou = False

while acertou == False:
    chute = int(input("Digite um numero: "))
    if chute > valor_aleatorio:
        print("Chute um valor mais baixo")
    elif chute < valor_aleatorio:
        print("Chute um valor mais alto")
    else:
        print( "Você acertou!")
        acertou = True