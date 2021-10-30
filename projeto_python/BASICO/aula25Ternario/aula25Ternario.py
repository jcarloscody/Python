login = False
msg = 'pode logar' if login else 'ñ pode'
print(msg)


idade=input('Digite a sua idade')

if not idade.isnumeric():
    print('Digite a sua idade')
else:
    idade = int(idade)
    maioridade = (idade>=18)
    msg2 ='você é de maior' if maioridade else 'vc é pivete'
    print(msg2)


nome = input('Digite seu nome')
print(nome or False or None or 0 or 'vc não digitou nada')

a = 0
b = None
c= False
d = []
e = {}
f = 22
g = "josue"

variavel = a or b or c or d or e or f or g
print(variavel)  #vai aparecer 22 pq o primeiro verdadeiro já fica, no caso f
