import os
#https://docs.python.org/3/library/functions.html#open

caminho_procura = input('Digite um caminho \n')
termo_search = input('Digite um termo para busca \n')

contador = 0

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho <kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho,2)
    return f'{tamanho} {texto}'



for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_search in arquivo:
            try:
                contador+=1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arq: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensao: ', extensao_arquivo)
                print('Tamanho: ', formata_tamanho(tamanho))
            except PermissionError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print('desconhecido' + e)

print()
print(f'{contador} arquivo(S) encontrado(S)')