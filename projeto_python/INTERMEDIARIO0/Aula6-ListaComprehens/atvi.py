carrinho = []
carrinho.append(('produto 1', 60))
carrinho.append(('produto 2', 55.90))
carrinho.append(('produto 3', '34'))
carrinho.append(('produto 4', 109.89))

total = sum([float(y) for x,y in carrinho])
print(total)


lista = [
    ('chave1', 'valor'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
]

d1 = {x: y for x,y in lista}
print(d1)


d2 = {x: y*2 for x,y in lista}
print(d2)


d3 = {x: y.upper() for x,y in lista}
print(d3)

set = {x for x in range(5)}
print(set)

dicionario = {f'chave {y}': y*2 for y in range(5)}
print(dicionario)