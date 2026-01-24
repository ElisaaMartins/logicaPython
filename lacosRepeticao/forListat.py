# for repetição - lista

nomes = ["joão", "amanda", "rafael", "carol"]
for nome in nomes:
    print(nome)


#Exiba somente os maiores de idade na tela
idades = [10, 15, 18, 34, 13, 14]

for idade in idades:
    if idade >= 18:
        print(f'{idade} é maior de idade')
    else:
        print(f'{idade} é menor de idade')