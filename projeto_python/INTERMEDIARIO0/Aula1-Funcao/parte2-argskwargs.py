def func(a,b,c="sem valor"):
    print(a,b,c)

func(1,2,4)
func(1,2)

lista = [1,2,3,4,5,6]
a1, b2, *c = lista  # estou desempacotando a lista
print(c) # o * serve para desempacotar nas funções e em listas
print(*lista)   #desempacotando

print("************************")
print("")
def func(*args, **kwargs):  #fazendo uma Aula3-Tupla. o que define é o *, por converção usa-se a palavra args ou kwargs
    # com **, neste caso serão argumentos com palavras chaves
    #**kwargs - são key words arguments - sao palavras chaves, argumentos nomeados como por ex nome="josue"
    #a Aula3-Tupla não pode ser alterada e vem entre (), diferente de lista que pode mudar e vem entre []
    print("Aula3-Tupla args: ", args)
    print("Aula3-Tupla args[0]: ", args[0])
    print("Aula3-Tupla len(args): ", len(args))
    args = list(args) #convertendo para lista
    print("Convertido para lista: ", args)
    if args [0] < 20: #add valores na lista
        args[0]=100
        print("como args[0] é menor que 20 então será 100 agora")
        print("lista: ", args)
    args = tuple(args)
    print("Convertido para Tupla: ", args)
    print("For na Aula3-Tupla: ", args)
    for v in args:
        print(v)

    print("*******************************")
    print("trantando com os kwargs - key words arguments")
    print("kwargs: ", kwargs)
    #print("kwargs['nome'] e kwargs['sobrenome']: ", kwargs['nome'], " ", kwargs['sobrenome'])    #uma forma de acesso rudimentar
    nome = kwargs.get('nome') #esse é o melhor jeito de acessar as chaves kwargs, pois não gera erros.
    sobrenome = kwargs.get('sobrenome')
    curso = kwargs.get('curso')
    if nome is not None:
        if sobrenome is not None:
            print("seu full nome é: ", nome, " ", sobrenome)
        else:
            print('seu nome é: ', nome)
    if curso is not None:
        print("seu curso é: ", curso)


func(*lista,1,2,3,4,5,6,7, nome="josue", sobrenome="carlos", curso="Sistemas de In"
    "formática")  #o * desempacota a lista para cada elemento ser independente na func

func(*lista,1,2,3,4,5,6,7,  sobrenome="carlos", curso="Sistemas de In"
    "formática")
