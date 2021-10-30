lista = ['eu', 'vencer', 'guerreiro', 5, 'vitória']


print(lista)
print(lista[-1])
print(lista[3])

lista[0] = 'você'
print(lista[0])

print(lista[0:3:1]) #[start, end, step]
print(lista[::2])
print (lista[::-1])#mostra a lista ao contrário

l1 = [1,2,3,4]
l2 = [5,6,7,8,9]
l3 = l1 + l2

print(f'lista 1: {l1}')
print(f'lista 2: {l2}')
print(f'lista 3: {l3}')

l1.extend(l2) #estende os valores do l1
print(f'extendendo a lista 1: {l1}')

l1.extend("josue")

l2.append(10) #inseri mais um item ao final
print(f'add mais um item a lista 2  no final : {l2}')

l2.insert(0,4.9) #inseri mais um item no local desejado , neste caso 0
print(f'add mais um item a lista 2 no começo: {l2}')
print('$$$$$$$$$$$$$$')

print(f'lista 1: {l1}')
print(f'lista 2: {l2}')

l2.pop(0) #exlui o índice 0
print(f'Excluindo o índice 0 da lista 2: {l2}')

del(l2[2:4]) #excluindo um intervalo
print(f'Excluindo um intervalo do índice 2:4 da lista 2: {l2}')

lista1=[1,2,43,5,6,7,4,65,42,78,333,5,7,2235,56]
print(f'lista1: {lista1}')
print(f'o máx da lista1 é: {max(lista1)}')
print(f'o mín da lista1 é: {min(lista1)}')

listarange = list(range(0,100)) #aqui criamos uma lista usando a função list com o objeto inteirável range. estamos inteirando
print(listarange)
listarange = list(range(0,500,5)) #0 a 500 com step de 5 em 5
print(listarange)

for i in listarange:  #estamos inteirando com a listarange
    print(i)

tipo = ['string', True, 4, -3.45]

for elemt in tipo:
    print(f'o tipo do elemet é {type(elemt)} e o seu valor é {elemt}')

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x=[['a', 'b', 'c'], [1, 2, 3]]
print (x[0])
print(x[0][1])
x[0] = []
print(x[0])
