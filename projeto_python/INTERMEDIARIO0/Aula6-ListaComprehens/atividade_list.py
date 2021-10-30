string = '123456789123456789123456789123456789123456789123456789123456789'

n = 9
contadores = [i for i in range (0, len(string), n)]
tuplas = [(i, i + n) for i in range (0, len(string), n)]
lista = [string[i:i + n] for i in range (0, len(string), n)]
raw = [f'string[{i}:{i + n}]' for i in range (0, len(string), n)]
retorno = '.'.join(lista)

print(f"contador: {contadores}")
print(' ')

print(f"tuplas: {tuplas}")
print(' ')

print(f'lista: {lista}')
print(' ')

print(raw)
print(' ')

print(f"retorno: {retorno}")