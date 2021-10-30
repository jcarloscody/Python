lista = [
    ('key', 'value'),
    ('key2','value2')
]

dic = {x.upper()*2:y*5 for x,y in lista}
print(dic)

dic2 = {f'key - {x}': x**5 for x in range(20)}
print(dic2)


#a diferença entre a lista e dic comprensao é sutil.