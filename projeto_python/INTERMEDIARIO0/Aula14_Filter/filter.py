from INTERMEDIARIO0.Aula13_Mapas.map import lista,produtos

print('\n')
filtro = filter(lambda x:x>4, lista)
print(f'da lista: {lista} os elementos maiores de 4 são: \n {list(filtro)}')

print('\n')
filtro_listcomprehension = [x for x in lista if x >4]
print(f'da lista: {lista} os elementos maiores de 4 são \n {list(filtro_listcomprehension)}')

print('\n')
def filtro_preco(produto):
    if produto['preco'] >  30:
        produto['e_caro'] = 'True'
    else:
        produto ['e_caro'] = 'False'


    if produto['e_caro'] =='True':
        return True

#    if produto['e_caro']
    #return produto

#filtro_preco = Filter(lambda p: p['preco'] > 30, produtos)
#print(f'os preços maiores de R$ 30,00 são:\n')
#for x in filtro_preco:
#    print(x)
print('Os preços mais caros são')
filtro_produto = filter(filtro_preco,produtos)
for y in filtro_produto:
    print(y)


