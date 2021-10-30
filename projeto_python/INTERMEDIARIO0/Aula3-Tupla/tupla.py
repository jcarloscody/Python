tupla = (1,2,43,4,1,34,'sfd',23,'josue')  #uma Tupla não pode ser modificada. pode colocar ou nao parênteses

print("tupla: ", tupla)
print("Tupla[4]: ", tupla[4])

for i in tupla:
    print(i)

print("tupla[3:]: ", tupla[3:])


tuplaSemParenteses = 1,2,3,4,5,6,7

tuplaDeUmElemento = 2,   #se tiver só um elemento deverá pôr virgula ao final

tuplaConcatenada = tuplaDeUmElemento + tuplaSemParenteses


#desenpacotando
t1, t2, t3, *_, t5 = tuplaConcatenada
print("t5: ", t5)

tuplaMultiplicativa = (1,2,4) * 10
print("tuplamultiplicativa", tuplaMultiplicativa)

#convertendo para lista
tuplaConcatenada = list(tuplaConcatenada)
tuplaConcatenada[0] = 'modifiquei esse valor'
print("conversao tupla-lista: ", tuplaConcatenada)
tuplaConcatenada = tuple(tuplaConcatenada)
print("conversao lista-tupla: ", tuplaConcatenada)
