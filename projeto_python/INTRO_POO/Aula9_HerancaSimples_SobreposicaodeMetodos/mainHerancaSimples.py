from classes import *

c1 = Cliente('Luiz', 45)
print(c1.nome, c1.idade)
print(f'c1: {c1.falar()}')

a1 = Aluno('Josue', 24)
print(a1.nome, a1.idade)
print(f'a1:{a1.falar()}')


c2 = ClienteVIP('Rose', 34)
print(f'{c2.falar()}')

c3 = ClienteVIPE('Rose', 34, 'CAROS' )
print(f'{c3.falar()}')