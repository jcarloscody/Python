from random import randint

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


numero  = str(randint(100000000, 999999999))

novo_cpf = numero #tbm poderia ser novo_cpf=cpf[:9] #elimina os dois últimos digitos
reverso = 10   # contador reverso
soma = 0

# loop do CPF
for index in range(19):
    if index>8:   # primeiro indice vai de 1 <= 9 ou 0-8 0,1,2,3,4,5,6,7,8
      index -= 9   # os primeiros 9 digitos

    soma += int(novo_cpf[index]) * reverso  #valor total da multiplicação

    reverso -= 1    #decrementa o contador
    if reverso < 2:
        reverso = 11
        d = 11 - (soma % 11)

        if d > 9:  # se o digito for maior que 9 o valor do digito será 0
            d = 0

        soma = 0 # a soma da multiplicação ficará zerado
        novo_cpf += str(d) # adiciona o novo digito

print(novo_cpf)