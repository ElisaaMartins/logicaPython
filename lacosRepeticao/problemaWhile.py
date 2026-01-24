# Cenário Real - Gerenciador de login simples

'''
Crie um gerenciador de login simples, com o máximo de 3 tentativas.
(teremos apenas um único usuário e senha permitido)

usuário - jhonatan
senha - C

Após 3 tentativas, se o usuário estiver errado exibir:
"Aguarde 30 mins antes de tentar novamente!"

se acertar o usuário e senha antes disso, exibir "Login feito com sucesso"
'''

usuário = ''
senha = ''
tentativas = 0

while (usuário != "jhonatan" and senha != "senha123") and tentativas < 3:
    usuario = input("Digite o usuario: ")
    senha = input("Digite a senha: ")
    tentativas +=1 

if usuário != "jhonatan" and senha != "senha123":
    print("Aguarde 30 mins antes de tentar novamente!")
else:
    print("login feito com sucesso")