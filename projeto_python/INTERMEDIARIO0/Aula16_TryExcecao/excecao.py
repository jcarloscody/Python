#aqui iremos tratar as exceções, as exceções são erros

try:
    a = {}
   # print(a[1])
    try:
        a +=1
    except:
        print()
except NameError as erro:
    print(f'erro: {erro}')
#except Exception as erro:
# pega qq erro. imagine da seguinte forma,se o erro for de indice tem lá, se o erro for de qq outra coisa tem este último
    #print('Erro inesperado')"""
except KeyError as  erro: #para dicionario
    print('Erro no índice')
except IndexError as erro: #para lista
    print(erro)
#except (IndexError, KeyError) as erro:    #dois erros
    #print(erro)"""
else: # o bloco else sempre será executado desde que o código não caia na except
   print('será o else executado sempre que o try for true')
   print(a)
finally:
    print('o finally sempre será executada')

print('bora continuar')
print('outra forma de ')