from INTERMEDIARIO0.Aula13_Mapas.map import lista, produtos
from functools import reduce



            # o acumulador está guardando o acumulador com inicial em 0 mais o item a cada laço
nova = reduce(lambda acumulador, i : i + acumulador, lista, 0)
print(f'total da lista: {lista}')
print(f'total da lista: {nova}')

preco = reduce(lambda t_preco, p: p['preco'] + t_preco, produtos, 0)
print(f'o total de preço foi: {preco} e \n a médio foi {preco/len(produtos)}')


