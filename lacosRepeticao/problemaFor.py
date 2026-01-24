'''
Validador de senhas

Problema:
Você trabalha em um sistema que precisa verificar se todas as senhas digitadas
por usuários são válidas.

Para uma senha ser válida, ela deve ter pelo menos 6 caracteres.    
'''

# len(variavel) -> quantidade de caracteres
# len(senha) -> 6 ou não

senhas = ['12345', "abcdef", '123456', "abc12"]
for senha in senhas:
    if len(senha) >= 6:
        print(f'senha válida {senha}: 6 caracteres')
    else:
        print(f'senha inválida {senha}: menos que 6 caracteres')