frase = 'o rato roeu a roupa do rei de roma e deixou ele pelado sem roupa, mas eu dei a minha ' \
        'roupa'
tamanho_frase = len(frase)
contador = 0
nova_string ='' #troquei

input_usario = input('Qual letra você quer maiúscula? \n') #troquei

while contador < tamanho_frase: #troquei
    print(frase[contador], contador)
    #nova_string += frase[contador]
    letra = frase[contador]
    if letra==input_usario:
        nova_string += nova_string.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
