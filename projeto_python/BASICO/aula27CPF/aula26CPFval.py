"""
cpf : xxx.xxx.xxx-ab
x * 10 = y      #           x * 11 = w
x * 9 =  y      #           x * 10 = w
x * 8 =  y      #           x * 9 = w
x * 7 =  y      #           x * 8 = w
x * 6 =  y      #           x * 7 = w
x * 5 =  y      #           x * 6 = w
x * 4 =  y      #           x * 5 = w
x * 3 =  y      #           x * 4 = w
x * 2 =  y      #           x * 3 = w
               #         -> a * 2 = w
soma = y                    soma = w
y1 = 11 - (y % 11)  #       w1 = 11 - (w % 11)
se y1 > 9                   b = w1
a = 0
"""
"""
CPF = 168.995.350-09     digito 1: 0      digito 2: 9
-------------------------------------------------------------------

1*10=10               #         1*11 = 11 <-
6*9=54                #         6*10=60
8*8=64                #         8*9=72
9*7=63                #         9*8=72
9*6=54                #         9*7=63
5*5=25                #         5*6=30
3*4=12                #         3*5=15
5*3=15                #         5*4=20
0*2=0                 #         0*3=0
                      #     ->  0*2=0
    297               #          343

11 - (297%11) = 11    #       11 - (343%11) = 9  
se 11 > 9=0           #
Digito 1=0            #       Digito 2=9

"""


while True:
    cpf = input('Digite um CPF:')

    if not cpf.isnumeric():
        print('Digite um número válido')
        continue

    if not len(cpf) ==11:
        print('Digite um CPF válido:')
        continue

    novo_cpf = cpf[:-2] #tbm poderia ser novo_cpf=cpf[:9]
    reverso = 10
    soma = 0

    for index in range(19):
        if index>8:
            index -= 9

        soma += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (soma % 11)

            if d > 9:
                d = 0

            soma = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)  #evita sequências 11111111111


    if (novo_cpf == cpf) and not sequencia:
        print('CPF VÁLIDO')
    else:
        print('CPF INVÁLIDO')
