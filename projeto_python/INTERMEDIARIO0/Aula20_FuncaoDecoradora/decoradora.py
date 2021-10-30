from time import time
from time import sleep

"""
def fala_io():
    print('oi')

fala_io()

variavel = fala_io()

variavel()"""


def master():
    def slave():
        print('sou slave')
    slave()

master()



print()
def master():
    def slave():
        print('sou slave')
    return  slave

v = master()
v()



print()
def master(funcao):  #funcao decoradora
    def slave():
        funcao("olá galera, estou decorado")
    return slave


@master  #decorador
def printer(v):
    print(v)

printer()



print()
print()

def velocidade(funcao):
    def interna(*args, **kwargs):

        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'a função {funcao.__name__} levou {tempo}ms para executar')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()