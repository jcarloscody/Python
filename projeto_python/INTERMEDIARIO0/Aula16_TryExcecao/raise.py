def devide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print(erro)

print(devide(1,0))



def devide2(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print('erro' ,erro)
        raise  #ideal para programadores que acaba lançando um segunda exceção.

try:
    print(devide2(1,0))
except:
    print("wee")

#CRIANDO A PROPRIA EXCECAO COM RAISE
def devide3(n1,n2):
    if (n2==0):
        raise ValueError ("erro de denominador. nao pode 0")
    return n1/n2

#capturando a exceção que criei na funcao devide3()
try:
    print(devide3(1,0))
except ValueError as erro:
    print(erro)


