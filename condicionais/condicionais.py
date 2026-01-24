'''syntaxe
if condicao:
    # código se verdadeiro
else:
    # código em qualquer outro caso
'''

#condicionails - if elif else



trabalho_terminado = True

if trabalho_terminado == True:
    print("Bora")
else:
    print("Não posso sair")


estou_livre = False
if estou_livre == False:
    print("ok bora mover as caixas")
else: 
    print('pede ajuda para o meu irmão')


#condicionails - if elif else

atrasos = int(input("quantas faltas você tem? "))
if atrasos >= 3:
    print ("você está suspenso")
elif atrasos == 2:
    print("mais uma falta e estará suspenso")
elif atrasos == 1:
    print("mais duas faltas e estará suspenso")
else:
    print("pode entrar")