# for é para coisas finitas e while para coisas que não sabemos

frase = 'sou um vencedor'

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
for letra in frase: # estamos inteirando a string finita
    print(letra)

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
for i, letra in enumerate(frase):  #isto não é índece, mas coincide
    print(i, letra)

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
for n in range(10): # esta é a função range. aqui temos range(start=0, stop, step=1)
    print(n) # por padrão o start é 0 e o step (de quantos em quantos ele pula) é 1

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
for n in range(2, 10, 2): # vai do dois a dez e pula de dois em dois
    print(n)
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
for x in range(30, 5, -1): # aqui ele decrementa. de 30 vai -1 até 5
    print(x)

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

for x in range(51):
    if x %2 ==0:
        print(f'par {x}')
    else:
        print(f'impar {x}')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

nome = 'Josue'
nom = ''
# pode colocar continue (pula p/ o próximo laço) ou break
for letra in nome:
    if letra=='u':
        # continue #ñ inclui a letra u
        nom += letra.upper()
    elif letra=='e':
        # break # quebra o laço
        nom += letra.upper()
    else:
        nom += letra

print(nom)