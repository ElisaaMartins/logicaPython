# Projeto 3: Medidor de Velocidade
'''
Crie um programa que receba do usuário um valor que represente a velocidade em
uma via cuja velocidade máxima permitida é de 80 km/h.

Com base nesse valor, o programa deve informar se o motorista levou 
uma multa leve, grave ou gravíssima.

Se a velocidade estiver abaixo ou igual a 80 km/h, exiba: "não houve multa".
Se estiver até 10 km/h acima, exiba: "levou multa leve".
Se estiver entre 11 km/h e 20 km/h acima, exiba: "levou multa grave".
Se estiver acima de 20 km/h, exiba: "levou multa gravíssima".
'''

velocidade = int(input("qual a sua velocidade: "))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print("não houve multa")
elif velocidade > velocidade_maxima and velocidade < 90:
    print("levou multa leve")
elif velocidade > 90 and velocidade < 100:
    print("levou multa grave")
elif velocidade > 100:
    print("levou multa gravíssima")

'''
if velocidade <= velocidade_maxima: 
    print('não houve multa')
elif velocidade <= velocidade_maxima + 10: 
    print('levou multa leve')
elif velocidade <= velocidade_maxima + 20: 
    print('levou multa grave')
else:
    print('multa gravíssima')
'''