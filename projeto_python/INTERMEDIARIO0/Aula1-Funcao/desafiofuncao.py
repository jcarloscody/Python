def saudacao(nome):
    print(nome,'Seja muito bem vindo a este joguinho')

def soma():
    a = input('Digite um número\n')
    try:
        a = float(a)
    except:
        print('Você não digitou valor válido. recomece!')

    b = input('Digite um número\n')
    try:
        b = float(b)
    except:
        print('Você não digitou valor válido. recomece!')

    c = input('Digite um número\n')
    try:
       c = float(c)
    except:
        print('Você não digitou valor válido. recomece!')

    return a + b + c



def perc():
    print('%%%%%%%%%%%%%%%%%%%%%%%  PERCENTAGEM')
    valor = float(input('Digite o valor\n'))
    percent= float(input('digite a percentagem\n'))
    resul = valor + (percent*valor/100)
    print(f'O aumento percentual do valor de R$ {valor} sob a percentagem de {percent} % é R$ {resul}')

def fizbuz():
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@   CONDICIONAL FIZBUZ')
    x = input('Digite um valor: \n')
    try:
        x = float(x)
        if x % 5 == 0 and x % 2 == 0:
            return 'FIZZBUZZ divisível por 5 e 2'
        if x % 2 == 0:
            return 'FIZZZ divisivel por dois'
        if x % 5 == 0:
            return 'BUZZZ divisível por 5'
        return x
    except:
        print('Você não digitou valor válido. recomece!')





#nome1 = input('Digite o seu nome:\n')
#saudacao(nome1)

#print(f'Vamos fazer um somatório, {nome1} $$$$$$$$$$$$$$$$$$$')
#soma = soma()
#print(f'a soma é: {soma}')
#perc()
print(fizbuz())