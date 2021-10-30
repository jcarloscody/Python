#CONJUNTO - é uma coleção de elementos que pode adicionar dentro de uma mesma estrutura de dados.
# mas os sets só suportam elementos únicos. não aceita elementos duplicados

#add (adiciona), update(atualiza), clear, discard
#union | (une)
#intersection & (todos os elementos presentes nos dois Sets)
# difference - (elemntos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois Sets, mas não em ambos)
# Sets ou conjunto
# não possuem chaves como o dicionário ou indixe como as listas
# não obedece ordem e não repete elementos


s1 = {1,2,4,5,6}

for v in s1:  #essa é a unica forma de acessar o set
      print(v)

s1.update('JOSUÉ')

s2 = set()  #fazendo um set vazio

s2.add(('jo',3,1000,'go')) #adicionando tupla
s2.add('KOR')
s2.add('jh')
s2.add(2)
s2.add(45)

#print(s1)
print(s2)

s2.discard('KOR')#deletar elementos
print(s2)

s2.update('JOSUÉ') #o update intera os elementos
print(s2)

lista = [3,3,3,3,5,4,32,5,5,'jo',43,'jo']
print(f'Esta é uma lista {lista}')
lista = set(lista)  #fazendo um catch de lista para set, pois na lista aceita elementos repetidos.
#e dessa forma queremos eliminar, como lista não aceita, fizemos este catch para set e depois voltamos para lista
lista = list(lista) # o problema é que provavelmente poderá vir fora de ordem.
print(f'Esta é uma lista depois do catch com set {lista}')

print(f'S1:   {s1}')
print(f'S2:  {s2}')
s3 = s1 | s2  #union uniao os Sets
print(f'União de S1 com S2   {s3}')
s4 = s1 & s2  #intersecção
print(f'Intersecção de S1 com S2    {s4}')
s5 = s1 - s2  # diferença do s1 para com o s2
s6 = s2 - s1 # diferença do s2 para com o s1
print(f'A diferença do S1 para com o S2 é   {s5} '
      f'\n A diferença do S2 para com o S1 é   {s6} ')

s7 = s1 ^ s2  #os elementos que não estão em ambos ao mesmo tempo
print(f'Os elementos que não estão em ambos ao mesmo são  {s7}')


# verificando igualdade entre lista com elementos repetitivos sem comprometer a composição
lista1 = [1,2,3,5,6,7]
lista2 = [1,1,1,2,3,5,5,6,7]  #aqui temos uma lista2 igual a lista1 porém com elementos repetitivos
# mesmo assim se fizermos um if dará falso
print(lista1==lista2)  #false
# mas usamos do set dentro do if para não fazermos catch e comprometer a composição
if set(lista1)==set(lista2):
      print('Listas iguais')
else:
      print('Listas diferentes')