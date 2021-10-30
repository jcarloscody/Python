secreto = 'vencedor'
digitadas = []
chances = 4

while True:
    if chances ==0:
        print('VOCÊ LOST')

        break

    letra = input('Digite a letra da palavra \n')

    if len(letra) >1:
        print('Ahh, meu velho, não vale. Digite uma só letra.')
        continue

    if letra.isnumeric():
        print('Ahh, meu velho, não vale. Digite uma letra.')
        continue

    if letra not in secreto:
        chances -= 1

    digitadas.append(letra)

    if letra in digitadas:
        print('Uhuuuu, Você acertou uma letra. Continue acertando.')
    else:
        print(f'Que peninha, a letra "{letra}" não faz parte. Tente outra vez')
        digitadas.pop()

    palavra_secreta = ''

    for letra_secreta in secreto:
        if letra_secreta == digitadas:
            palavra_secreta += letra_secreta
        else:
            palavra_secreta += '*'

    if palavra_secreta == secreto:
        print('você ganhou!!!!!!')
        print(palavra_secreta)
        break
    else:
        print(f'Continue tentando. {palavra_secreta}')

    print(f'Você ainda tem {chances} chances \n')