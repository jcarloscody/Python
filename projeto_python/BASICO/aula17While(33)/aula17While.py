# laço while (enquanto)




while True:
    x=1

    voltas = int(input('Digite o número de voltas'))
    while x<= voltas:
        x += 1
        nome = input('qual o seu nome')

        print(f'olá, {nome}. ********** VOCÊ É UM WINNER!!!!!!!!!!')
        if x>voltas:
            y = int(input('Digite : \n 0 - sair \n 1- sair de tudo'))
            if y ==0:
                break  # SAI DO LAÇO
    if y==1:
        break






x=0
while x<5:
    if x==2:
        x += +1
        continue  # o continue serve para não executar as linhas posteriores, ou seja, volta. neste caso não mostra a linha 2
    print(x)
    x += +1

print('acabou')

a=0
while a<5:
    if a==2:
        a += +1
        break  # termina o código do laço
    print(a)
    a += +1

print('acabou')


x=0
while x<10:
    y = 0
    while y<5:
        y+=+1
        print(f'{x}, {y}')
    x+=+1

# CALCULADORA


x = True

while x:
    n1 = input('digite um valor')
    n2 = input('digite outro')
    try:
        n1=float(n1)
        n2=float(n2)
    except:
        print("Digite um numero")
        continue

    if not n1.isdecimal() or not n2.isdecimal():
        print('Digite um numeral')
        continue


    operador = input('Qual operador vc deseja: \n / \n * \n - \n + \n ou 0 para sair \n')

    if operador=='/':
        resultado = n1 / n2
        print(f'O resultado é {resultado}')
    elif operador=='*':
        resultado = n1 * n2
        print(f'O resultado é {resultado}')
    elif operador=='+':
        resultado = n1 + n2
        print(f'O resultado é {resultado}')
    elif operador=='-':
        resultado = n1 - n2
        print(f'O resultado é {resultado}')
    elif operador=='0':
        break
