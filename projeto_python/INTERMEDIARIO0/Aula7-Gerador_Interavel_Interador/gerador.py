import sys
import time

#interador   :::   é aquele que vai iterar para mostrar cada valor do interável, como por exemplo o for. ele converte em tempo de execução
#a string ou tupla (...) em um interador.  ele utiliza o next() até o interador esgotar, quando chegar ao fim
#uma exceção será levantada e aí ele para.

#interável:::  uma lista é interável, string, tupla são interável, mas numero nao

#gerador ::: serve para otimizar a memória. em vez de ocupar a memória
# com um tufão de coisas ao mesmo tempo, o gerador vair fazer com que o recurso esteja
# disponível apenas com aquilo que precisamos.  ao contrário do for, o gerador é consumido em tempo de execução.


#interável
a= "josue"
n = 1234
print(f"a string a é interável: {hasattr(a, '__iter__')}")
print(f"os numeros  da variável n é interável: {hasattr(n, '__iter__')}")




print("")
print("Usando o for para iterar")
#usando o for para interar
for i in a:
    print(i)




print("")
print("Iterando diretamente. convertendo para iter")
aa="aosidosindon"
#convertendo para interador para interar
interador = iter(aa)
print(next(interador))
print(next(interador))
print(next(interador))

print("")




print("consume de memória: ", sys.getsizeof(a))

print("")



#simulando um gerador
print("")
print("simulando um gerador: como se estivesse algo pesado carregando")

def gera1():
    r = []
    for n in range(10):
        r.append(n)
        time.sleep(0.1)
    return r

g1 = gera1()
for i in g1:
    print(i)




#GERADORR
def gera():
    for n in range(10):
        yield n
        time.sleep(0.1)

g = gera()
print("")
print("GERADOR")
for v in g:
    print(v)

#print(next(g))
#print(next(g))
#print(next(g))


def gera2():
    v = 'v1'
    yield v
    v = 'v2'
    yield v
    v = 'v3'
    yield v
    v = 'v4'
    yield v
    v = 'v5'
    yield v


g2 = gera2()

print(next(g2))
print(next(g2))

for y in g2:
    print(y)

l1 = [x for x in range(1000)]
print(f"tipo: {type(l1)} com {sys.getsizeof(l1)} de memória")
l2 = (x for x in range(1000))      #GERADOR mais sintetico
print(f"tipo: {type(l2)} com {sys.getsizeof(l2)} de memória")



nome = 'josu3e carlos'
interador_nome = iter(nome)
