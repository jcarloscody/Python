# indices das strings
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/functions.html


# positivo       0-o 1-l 2-a 3-(espaço)  4-j
texto = 'olá j'
# negativo  -5-o -4-l -3-a -2-(espaço)  -1-j

nome = 'josue carlos da silva'
print(texto[2])  # aparecerá apenas o índice 2 - á
print(texto[2:4])  # aparecerá apenas os índices 2-á e 3- (espaço)
print(texto[:3])  # aparecerá apenas os índices 0 a 2
print(texto[2:])  # aparecerá apenas os índices 2 até o final
print(texto[:-1])
print(nome[:])

print(f'quantidade de caracter da variável NOME: {len(nome)}')  #quant de caracter

print(nome[0:21:2]) #aquie ele vai do início até o fim pulando de dois em dois termoaquo:termoadquem:pulos
print(nome[0::3]) #aquie ele vai do início até o fim pulando de três em três
print(nome[::4]) #aquie ele vai do início até o fim pulando de quatro em quatro


t = nome[:2]
print(t)