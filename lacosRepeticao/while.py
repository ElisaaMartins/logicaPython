#laços de repetiçao - while
# não fixo, O laço repete enquanto a condição for verdadeira (True), 
# atualizar variavel de controle para não ter loops

''' syntaxe
while condicao:
    # código a ser executado
'''

# um sistema que permite 3 tentativas antes de fechar

tentativas = 0
while tentativas < 3:
    print("tente novamente")
    tentativas = tentativas + 1 

# Só pode logar, se digitar a senha correta
senha = ''

while senha != '123456':
    senha = input("Digite a senha correta: ")

print("Bem vindo")