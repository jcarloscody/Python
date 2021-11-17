"""split, enumerate, join"""

string = 'O Brasil é o o, o o país, da bola,o Brasil é penta na bola .'

lista1 = string.split(' ') # faz separação entre as palavras criando uma lista a partir de uma str
print(lista1)
lista2 = string.split(',')
print(lista2)
"""print(lista1)

palavra=''
contagem =0
for letra in lista1:
    #print(f'a palavra "{letra}" apareceu {lista1.count(letra)} x')
    quantidade = lista1.count(letra)

    if quantidade>contagem:
        contagem = quantidade
        palavra=letra

print(f'a palavra {palavra} apareceu mais vezes {contagem} x')"""

string2 = ' '.join(lista1) #cria uma string a partir de uma lista
print(f'esta é a lista {lista1}')
print(f'esta é a string2: "{string2}"')

for indice, valor in enumerate(lista1): #vai enumerar a lista. a forma é FOR ÍNDICE, VALOR
    print(indice, valor) # o enumereite simplifica a vida da equação abaixo

for v1 in enumerate(lista1):
    indice, valor = v1
    print(indice)

EQ = 'ENUMERAÇÃO NÃO SIMPLIFICADA'
print(f'{EQ:%^40}')
l = [
    [0, 'jos'],
    [1,'car'],
    [2,'kkk']
]

print(l[0])
for indice, nome in l:
    print(indice, nome)