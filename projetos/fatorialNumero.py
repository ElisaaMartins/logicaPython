# Projeto 1 - Fatorial de um número
# Crie um programa que recebe um número e imprime o seu fatorial.

numero = input("digite um numero: ")
fatorial = 0

if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero+1):
        #print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
    print(f'O fatorial de n é {fatorial}')
else: 
    print("Informe apenas números inteiros positivos")

'''
numero = int(input('Digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero+1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
    print(f'o fatorial de {numero} é {fatorial}')
else:
    print('favor informar apenas números inteiros positivos')
'''