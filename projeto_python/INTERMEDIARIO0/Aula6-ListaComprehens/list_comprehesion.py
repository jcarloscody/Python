l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [v for v in l1]
print(f'LISTA EX1:  {ex1}')

print(" ")

ex2 = [v*3 for v in l1]
print(f'LISTA EX2:  {ex2}')

print(" ")

ex3 = [(v,v2) for v in ex2 for v2 in range(5)]
print(f'LISTA EX3:   {ex3}')
print(f'LISTA EX3[1]:   {ex3[1]}')

print(" ")

l2 = ['josue','lucas', 'salomao','jose','jonadarque','moura']
ex4 = [v.replace('o','@').upper() for v in l2]
ex5 = [v.replace('a','@') for v in ex4]
print(f'LISTA ex5 (replace):    {ex5}')

print(" ")

tupla = (
    ('chave','valor'),
    ('chave2','valor2'),
)
ex66 = [(x,y) for x,y in tupla]
print(f'tupla ex66:  {ex66}')

re = []
ex6 = [(y,x) for x,y in tupla]
print(f'tupla ex66 invertido ex6:  {ex6}')

ex66 = dict(ex66)
print(f"convertendo tupla ex66 para dicionario: {ex66}")

print(" ")

lista2 = list(range(100))
print(f'lista2: {lista2}')
ex7 = [v for v in lista2 if v % 2==0 if v%4==0]
print(f'DIVISIVEIS POR 2 E 4  EX7:   {ex7}')
ex8 = [v if v%5==0 or v%6==0 else (f'{v} fora') for v in lista2]
print(f'DIVISIVEIS POR 5 E 6 EX8:  {ex8}')