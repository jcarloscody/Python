nome = input('Digite o seu nome: ')

quant_caract = len(nome)

texto = input('digite um texto')

#em python tudo é objeto, desta forma sempre tem um método atrelado
print('o total de caracteres são ' ,texto. __len__())
print(f'o nome {nome} possui {quant_caract} caracteres e o tipo é {type(nome)}')
print(f'o total de caracteres é {texto.__len__() + quant_caract}')

if quant_caract <10:
    print('O nome é pequeno demais')
else:
    print('ta bom')