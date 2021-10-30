#count - vai retornar um iterador, vai gerar um contador que pode iterar, diferente da função range que é um iteravel mas nao um iterador

from itertools import count

contador = count()  #iterador que nao tem fim. 0 1 2 3 4 5 ...

for valor in contador:
    print(valor)
    if valor > 10:
        print("se não tivesse esse break iria travar o pc om loop infinito")
        break



contador2 = count(start=10, step=20)  #iterador que nao tem fim. 0 1 2 3 4 5 ...

for valor in contador2:
    print(valor)
    if valor > 500:
        print("se não tivesse esse break iria travar o pc om loop infinito")
        break

contadorinverso = count(start=10, step=-1)  #iterador que nao tem fim. 0 1 2 3 4 5 ...

for valor in contadorinverso:
    print(valor)
    if valor < 0:
        print("se não tivesse esse break iria travar o pc om loop infinito")
        break



