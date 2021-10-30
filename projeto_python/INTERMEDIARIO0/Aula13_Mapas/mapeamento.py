from INTERMEDIARIO0.Aula13_Mapas.map import lista, produtos, pessoas

#quando trabalhamos com map(x y) o x sempre é uma função depois vem o argumento
print('\n')
print('Retornando multiplicação da lista')
nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))

new_lista = [x * 2 for x in lista]
print(new_lista)

print('\n')
print('Retornando só o preço **********************')
precos = map(lambda x: x['preco'], produtos)  #retornando só um valor
for preco in precos:
    print(f'R$: {preco}')

print('\n')
print('Aumentando o Preço  *************************')
def aumenta_preco (p):
    p['preco'] = round(p['preco'] * 1.05,2)
    return p

novo_preco = map(aumenta_preco, produtos)

for precon in novo_preco:
    print(precon)

print('\n')
print('Monstrando Pessoas  *************************')
nome = map(lambda n : n['nome'], pessoas)
for x in nome:
    print(f'nome: {x}')

print('\n')
print('######## Mostrando Idades')
idade = map(lambda i: i['idade'], pessoas)
cont = 0
for i in idade:
    print(f'idade: {i}')
    if i >=60:
        cont += 1
print(f'a quantidade de idosos são: {cont}')

print('\n')
conte_idoso = 0
conte_jovem = 0
def nova_idade(i):
    if i['idade'] >= 60:
        i['status'] = 'idoso'
    if i['idade']< 60:
        i['status'] = 'jovem'
    return i

tabela = map(nova_idade,pessoas)
for tab in tabela:
    print(tab)
    if tab['status'] == 'idoso':
        conte_idoso += 1
    if tab['status'] == 'jovem':
        conte_jovem += 1
print(f'A quantidade de Jovens são: {conte_jovem}')
print(f'A quantidade de Idosos são: {conte_idoso}')

