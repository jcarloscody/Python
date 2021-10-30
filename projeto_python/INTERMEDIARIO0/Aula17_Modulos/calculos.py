import  math

PI = math.pi

def dobra(lista):
    return [x*2 for x in lista]

def mul(lista):
    r =1
    for x in lista:
        r *= x
    return r


if __name__ == '__main__':   #aqui esta dizendo que se importar este aqui, este codigo de baixo nao deve ser exe juntamente
    lista = [1,2,3,4,5]
    print(dobra(lista))
    print(mul(lista))
    print(PI)