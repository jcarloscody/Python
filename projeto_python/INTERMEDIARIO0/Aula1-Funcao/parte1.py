"""funções - def em python"""
# se eu não uso os parênteses da função, ela não é executada.


def SaudacaoInicial():
    print('hello world')

SaudacaoInicial() #chama a função

def saudacao (msg='olá',nome='usuario' ):  # pode pôr variável dentro do parâmetro e pode se quiser pôr um valor padrão
    msg = msg.replace('e','3')
    nome = nome.replace('o','5')
    print(msg, nome)

saudacao() #chama a função. não colocou nada pq já tem um valor padrão
saudacao(nome='Josué Carlos', msg='Olá meu querido amigo')
saudacao('Olá meu querido amigo', 'Josué Carlos')  # os parâmetros devem ser postos em ordem, já que não tem especificação

def saudacao2(nome1='josue', msg1 ='bem vindo'):
   return f'{nome1} {msg1}'

variavel = saudacao2()
print(variavel)

def funcaox(var):
    print('vsdmvosidmovi')
    return var

variavel = funcaox('olaaaaaaaaaaa')

def divisao (a,b):
    if b==0:
        return
    return a/b

a1 = float(input('Digite um número'))
b1 = float(input('Digite um número'))

resultado = divisao(a1,b1)
if resultado:
    print(resultado)
else:
    print('Todo número divido por 0 é 0.')
