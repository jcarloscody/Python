from itertools import groupby, tee

alunos = [
    {'nome':'luiz', 'nota':'A'},
    {'nome': 'lucas', 'nota': 'C'},
    {'nome': 'silva', 'nota': 'D'},
    {'nome': 'carlos', 'nota': 'B'},
    {'nome': 'jo', 'nota': 'A'},
    {'nome': 'iviston', 'nota': 'D'},
    {'nome': 'shuratey', 'nota': 'E'},
    {'nome': 'mamamia', 'nota': 'C'},
    {'nome': 'licon', 'nota': 'E'},
    {'nome': 'licon', 'nota': 'C'},
    {'nome': 'licon', 'nota': 'A'},
    {'nome': 'licon', 'nota': 'D'},
    {'nome': 'licon', 'nota': 'D'},
{'nome': 'licon', 'nota': 'B'},
{'nome': 'licon', 'nota': 'C'},
{'nome': 'licon', 'nota': 'E'},
]

"""alunos.sort(key=lambda i:i['nota'])
for alunos in alunos:
    print(alunos)"""


ordena = lambda x:x['nota']
alunos.sort(key=ordena)


"""for nota, agrupamento in groupby(alunos,ordena):
    print(f'Agrupamento de : {nota}')
    for aluno in agrupamento:
        print(aluno)
    print()"""

for nota, agrupamento in groupby(alunos,ordena):
    print(f'Agrupamento de : {nota}')
    v1,v2 = tee(agrupamento)
#o tee faz a cópia do iterador. assim eu posso usar mais de uma vez
    for gruop in v1:
        print(gruop)
    quantidade = (f'{len(list(v2))} tiram nota {nota}')
    print(f'{quantidade} tiram nota {nota}')

    print()