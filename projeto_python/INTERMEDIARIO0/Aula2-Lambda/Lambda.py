
#lambda são funções anonimas

def SomaDivisao(x,y,z):
    return (x + y)/z

FuncaoAnonima = lambda x,y,z: (x + y)/z

print(FuncaoAnonima(2,10,5))

print(SomaDivisao(2,10,5))



Listaprecos = [
    ['p1', 2],
    ['p2', 900],
    ['p3', 712],
    ['p4', 11],
    ['p5', 234],
    ['p6',33]
]

#ordenando a lista    | se usar a funcao sort direto na lista preco não vai funcionar, pois como
# tem dentro da lista outras listas o interpretador nao sabe fazer desta forma, para isto criaremos uma funcao.

def ordenandoLista(item):
    return item[1]

"""Listaprecos.sort(key=ordenandoLista())
Listaprecos.sort(key=ordenandoLista(), reverse=True)"""

#ordenando com lambda sem precisar criar funcao
Listaprecos.sort(key=lambda item:item[1], reverse=True)
Listaprecos.sort(key=lambda item:item[1])
print(sorted(Listaprecos, key=lambda i: i[1], reverse = False))

