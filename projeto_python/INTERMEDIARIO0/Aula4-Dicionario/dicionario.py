dicionario = {'chave1': 'valor da chave',}  #no dic colocamos o indice e seu valor
print(dicionario)

# a chave deve ser única
dicionario ['nova_chave'] = 'valor da nova_chave'  #add novo valor
print(dicionario['chave1'])

dicionario['nova_chave'] = 'eu alterei o valor da nova_chave' #alterando valores
dicionario.update({'b':'tu vaie'})   #add novo valor

#nova forma de fazer dicionario
dicionarioNovo = dict(chave1='valuekey1',chave2='valuekey2',chave3='valuekey3',chave4='valuekey4')

dic = {1:'jsoue', 2:'timbabu', 3:'perna', 'a':'timbora'}
dic['a'] = 'vamos'  #alterando valor
dic.update({'b':'tu vaie'})   #add novo valor
print(dic)

#verificando se a chave existe para não dar um catch error
if 'chave5' not in dicionarioNovo:
    print("chave5 nao existe no dicionarioNovo")
else:
    print("chave5 existe no dicionarioNovo", dicionarioNovo['chave5'])


if 'chave4' in dicionarioNovo:
    print("chave4 existe no dicionarioNovo", dicionarioNovo['chave4'])
else:
    print("chave4 não existe no dicionarioNovo")


print(" ")
print(" ")
print("valor da chave josue", dicionarioNovo.get('nome'))

print(" ")
print(" ")
if dic.get('b') is not None:
    print(dic.get('b'))



del dic ['a']  #DELETANDO CHAVE
print(dic)

print(" ")
print(" ")
print('nome' in dicionarioNovo)  # se existe a chave no dicionario
print('nome' in dicionarioNovo.keys()) # se existe a chave no dicionario
print('josue' in dicionarioNovo.values()) #checa se tem o valor josue dentro do dicionario


print(" ")
print(" ")
print(len(dicionarioNovo))  #quantidade de pares chave-valor


print(" ")
print(" ")
#inteirando com chaves
for k in dicionarioNovo:
    print(k)

print(" ")
print(" ")
#inteirando com valores
for k in dicionarioNovo.values():
    print(k)


print(" ")
print(" ")
#inteirando com chaves-valores
for k in dicionarioNovo.items():
    print(k)


print(" ")
print(" ")
#inteirando com chaves-valores separadamente
for k in dicionarioNovo.items():
    print(k[0], k[1])


print(" ")
print(" ")
#inteirando com valores
for k, w in dicionarioNovo.items():
    print("chave: ", k)
    print("valor: ", w)





"""print(3 in dic.keys())
print(3 in dic)  #mesma coisa supra
print('perna' in dic.values())

print(f'o dic possui {len(dic)} pares de elementos')

for k in dic:
    print(k)  #só mostra as chaves

for v in dic.values():
    print(v)  #só mostra os valores

for k in dic.items():
    print(k)  #mostra os valores e chaves

for k,v in dic.items():
    print(v, k)  #manipulando valores e chaves de forma independente
    print(v)
"""
print(" ")
print(" ")


clientes = {
    'clientes_timbauba': {
        'josue' : 'rua canario',
        'eliane' : 'rua do moco',
        'josé' : 'rua do pinicano',
        'eliz' : 'rua benedito'
    },
    'Clientes_aliança' : {
        'Carlinha' : 'rua tu tá conosco',
        'Leninha' : 'rua severina da nobrega'
    },
    'Clientes_RJ':{
        'Juliana' : 'rua tmj',
        'Otavio':'rua alejadinho'
    }
}

for k, j in clientes.items():
    print(f'estes são os dicionário {k}')
    for valores in j.items():
        print(f'\t {valores}')



print(" ")
print(" ")

import copy  #para copiar de forma real profunda
dic2 = copy.deepcopy(dic)  #se quiser copiar é importante usar este termo, pois só o = não basta.façao teste
dic2[1] = 'josue carlos'
print(dic2)
print(dic)

print(" ")
print(" ")

dic2.pop('b')  #elimina o item indicado pela chave
print("valor b elimitado: ", dic2)
dic2.popitem()  #elimina o último item de cara
print("ultimo item eliminado: ", dic2)