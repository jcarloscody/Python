import json


print()
print('CONVERTENDO ARQUIVO JSON PARA DICIONARIO')
with open('json.json', 'r') as jsondic:
    dic = jsondic.read()
    dic = json.loads(dic)


print( dic)

for v,k in dic.items():
    print(v)
    for i,f in k.items():
        print(i,f)
    print()