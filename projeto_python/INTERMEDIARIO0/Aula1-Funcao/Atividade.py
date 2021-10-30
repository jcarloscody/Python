#CRIE UMA FUNCAO1 QUE RECEBE UMA FUNCAO2 COMO PARAMETRO E RETORNE O VALOR DA FUNCAO2 EXECUTADA
def olamundo():
    return 'Olá munodo'

def mestre(funcao):
    return funcao()

x = mestre(olamundo)
print(x)


#crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada. faca a
# funcao1 executar duas funcoes que recebem um numero diferente de argumentos.
def mestre2(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def falaoi(nome):
    return f'Oi {nome}'

def saudacao (nome, sobrenome, saudacao ):
    return f'{saudacao} {nome}'

exe = mestre2(falaoi, 'josue')
print(exe)

exe2 = mestre2(saudacao, 'josue','carlos',  saudacao='bom dia')
print(exe2)