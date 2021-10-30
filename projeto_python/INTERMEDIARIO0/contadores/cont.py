from itertools import count

contador = count(start=0, step=1)
#o step são de quantos em quantos

for valor in contador:
    print(round(valor,2))
#round  arredonda o valor
    if valor == 10:
        break

cont = count(1)
list1 = ['eu','amo','minha','terra','natal','que','saudade']
lista = zip(cont,list1)
print(list(lista))