variavel = 'nome'  # aqui temos uma variável global
variavel2 = 'nome'

def func():
    print(variavel)

def func2():
    variavel = 'carlos'  #aqui estamos criando uma variável privativa a esta função
    print(variavel)

func()
func2()

def func3 ():
    global variavel
    variavel = 'josue carlos'  #aqui não estamos criando uma variável privada, mas pegando aquela variável global
    # e alterando o valor dela. OBS isto não é recomendado
    print(variavel)


func3()

#tratando a variável global dentro da funcao
def func4(arg=None):
    arg = arg.replace('n','t')
    return arg

r = func4(variavel2)
print(r)


