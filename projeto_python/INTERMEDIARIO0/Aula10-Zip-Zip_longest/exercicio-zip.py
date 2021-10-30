"""considerando duas listas de inteiros, some os valores nas listas retornando uma nova lista com os valores
somados:

"""



lista_A= [1,2,4,5,6,7]
lista_B = [1,2,3]

"""listaSoma = []
for i in range(len(lista_B)):
    listaSoma.append(lista_A[i] + lista_B[i])
print(listaSoma)"""

"""listaSoma2 = []
for i, _ in enumerate(lista_B):    # _ quer dizer que não quer determinado valor
    listaSoma2.append(lista_A[i] + lista_B[i])
print(listaSoma2)"""

listaSoma3 = [(x+y) for x,y in zip(lista_A, lista_B)]
print(listaSoma3)
