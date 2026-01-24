# listas 
# coleções ordenadas que podem armazenar múltiplos valores

'''
indice
[20, 50, 100]
  0   1   2
'''
precos = [20, 50, 100]
print(precos[0]) #20

# encontra indice automatico - index
nomes = ["Brasil", "EUA", "Mexico"]
print(nomes.index("EUA")) #1

# manipular - add itens
salarios =[2500, 10000, 300]
salario_usuario = float(input("qual seu salario "))
salarios.append(salario_usuario)
print(salarios)