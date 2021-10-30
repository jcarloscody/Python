varavel = ['Luiz Otavio', 'joaozinho', 'Maria', 'Josué']

comeca_com_j = False
letraj = '\n'
#o for tem o break e o continue tbm


for letra in varavel:
    if letra.lower().startswith('j') or letra.startswith('J'):  #o startswith é uma função que checa se uma palavra começa com um caracter específico
        comeca_com_j=True
        letraj += letra + '\n'


if comeca_com_j:
    print('Comeca com J', letraj)
else:
    print('ñ comeca')
