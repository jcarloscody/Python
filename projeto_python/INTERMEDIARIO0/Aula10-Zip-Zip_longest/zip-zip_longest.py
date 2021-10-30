"""zip - unindo iteráveis
zip_longest - do pacote itertools

zip - uni lista mas de forma limitada. retorna um gerador"""


from itertools import  zip_longest, count     #funcao zip_longest

indice = count()

cidades = ['sao paulo', 'recife', 'belo horizonte', 'salvador', 'alianca']

estados = ['sp','pe','mg']

cid_uf = zip(estados, cidades)

"""for x, y in cid_uf:
    print(x, y)"""

"""for valor in cid_uf:
    print(valor[0], valor[1])"""

"""print(cid_uf)  #como é iterável, vai mostrar só o objeto

cid_uf = list(cid_uf)
print(cid_uf)"""


cida_uf = zip_longest(estados, cidades)
print(list(cida_uf))

print()
cidad_uf = zip_longest(estados, cidades, fillvalue="uf")
print(list(cidad_uf))

#estou usando o zip pq estou usando o indice. o indice é um gerador e por estar gerando infinitamente indices, se eu der um for então dará um loop infinito se colocar o zip_longest.
cidade_uf = zip(indice, estados, cidades)
for valor in cidade_uf:
    print(valor)