"""COMBINATIONS, PERMUTATIONS, PRODUCT - ITERTOOLS
Combinations - ordem nao importa
Permutacao - ordem importa
ambos nao repetem valores únicos
Product - ordem importa e repete valores unicos"""

from itertools import combinations, count, permutations, product

contador = count(1)

nome = ['thais', 'tayanne', 'scarlate', 'dani','marcos', 'jose','love']

print('a ordem Ñ importa ************** COMBINATIONS\n')
for combinacao in combinations(nome,2):
    print(combinacao)

print('\n')
print('a ordem  importa **************** PERMUTATIONS\n')
for comb2 in permutations(nome,2):
    print(f'{comb2}')

print('\n')
print('a ordem ñ importa e repete valores *********** PRODUCT \n')
for comb3 in product(nome,repeat=2):
    print(comb3)


