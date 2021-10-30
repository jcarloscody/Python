# FORMATANDO VALORES COM MODIFICADORES.
#
# :s - texto string
# d: - inteiros
# :f - float
# :. (numero)f - quantidade de casas decimais (float)
# :(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)
# > esquerda
# < direita
# ^ centro

nome ='josue carlos'
n=7
n2=34
t=n2/n
a = 2

print(t)
print('{:.2f}'.format(t))  #delimitando o nº de casas decimais
print(f'{t:.2f}')

print(f'{nome:s}')  # formatando dizendo que a variável é string

print(f'{a:0>10}')  #está delimitando o nº de casas dentro da variável e dizendo a composição das casas vázias
print(f'aquiiiiiii {a:0^11}')  #está delimitando o nº de casas dentro da variável e dizendo a composição das casas vázias

print(f'{nome:%^50}')
print(len(nome))
print(f'{nome:@>13}')
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa{:0>15}'.format(nome, a, t,))

nomeformatado = '{:@>50}'.format(nome)
print(nomeformatado)


print(nome.ljust(30,'#'))  #justifica
#nome= nome.ljust(30,'#')

print(nome.upper())  #maiúscula
print(nome.lower())  #minu
print(nome.title())  #título
