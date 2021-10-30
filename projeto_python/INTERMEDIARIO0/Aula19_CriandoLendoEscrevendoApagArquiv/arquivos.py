"""
r -  open for reading
w  - open for writing truncating the file first
x - open for exclusive creation, failing if the file already exist
t  - text mode
+ - open a disk file for updating

docs.python.org/3/library/functions.html#open
"""
import  os #import para remover arquivos
import json

# w+   abrir e escrever
file = open('abc.txt', 'w+')


file.write('Linha1 \n')
file.write('Linha2 \n')
file.write('Linha3 \n')

file.seek(0,0)  #para ler do topo do arquivo
print(file.read())

file.seek(0,0)  #para ele comecar a ler do topo de novo
print(file.readline(), end='')
print(file.readline())


file.seek(0,0)
print(file.readlines())

print()
file.seek(0,0)
for i in file.readlines():
    print(i, end='')

print()
file.seek(0,0)
for i in file:
    print(i, end='')


file.close()   #DEVE fechar o arquivo

print('ARQUIVO 2 ********************** - NÃO ACONSELHAVEL FAZER ASSIM')

try:
    file2 = open('cba.txt', 'w+')
    file2.write('Linha')
    file2.seek(0)
    print(file2.read())
finally:
    file2.close()



print()
print('ARQUIVO 3 ********************** - jeito mais correto de trabalhar com abertura de arquivos')
with open('def.txt', 'w+') as file3:
    file3.write('Linha 1\n')
    file3.write('Linha 2\n')
    file3.write('Linha 3\n')

    file3.seek(0)
    print(file3.read())

    #não precisa fechar com esta forma, pois ele se fecha sozinho



print()
print('apenas leitura')
with open('def.txt', 'r') as file3:
    print(file3.read())


print()
print('adicionando linhas sem apagar tudo')
with open('def.txt', 'a+') as file3:
    file3.write('outra linha\n')
    file3.write('outra linha\n')
    file3.write('outra linha\n')
    file3.seek(0)
    print(file3.read())


os.remove('abc.txt')


d1 = {
    'pessoa1': {
        'nome':'luiz',
        'idade':25,
    },
    'pessoa2': {
        'nome': 'rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True) #convertendo para json
print(d1_json)

print()
print('PODE CRIAR UM ARQUIVO JSON TBM USANDO O FILE')
with open('json.json', 'w+') as json:
    json.write(d1_json)
    json.seek(0)
    print(json.read())







