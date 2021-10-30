#problemas em ter objetos mutáveis
#objetos mutáveis: lisas dicionários
#objetos imutaveis: tuplas, strings, numeros, True, False, None

def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes([1,2,3])
clientes2 = lista_de_clientes([4,5,6])

print(clientes1)
print(clientes2)
