#  funções que irão verificar a tipagem do valor, se podem ou
#  não converter.
#  irá ajudar se podem
#  ou não fazer
# algo. verificar se o valor '1' é numerico ou não
# isnumeric, isdigit, isdecimal-> checa apenas se é nº e positivo


nt= input('digite um valor')
n2t=input('digite outro')

if nt.isnumeric() and n2t.isnumeric():  #SÓ CHECA NÚMERO E POSITO
    nt = int(nt)
    n2t = int(n2t)
    print(nt+n2t)
else:
    print("erro")


try:
    nt=float(nt)
    n2=float(n2t)
    print(nt+n2t)
except:
    print('erro')




# USANDO AS FUNÇÕES DO PROFESSOR
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

n= input('digite um valor')
n2=input('digite outro')

if is_number(n) and is_number(n2):
    n=float(n)
    n2=float(n2)

    print(n+n2)
else:
    print('erro')

