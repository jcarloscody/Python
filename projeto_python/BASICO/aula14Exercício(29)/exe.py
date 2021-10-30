numint = input('digite o valor inteiro')



if numint.isdecimal():
    numint=int(numint)

    if (numint % 2==0):
        print('O número digitado é INTEIRO e é PAR')
    elif  (numint % 2 != 0):
        print('O número digitado é INTEIRO e é IMPAR')
else:
    print('não é decimal')