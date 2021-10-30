# if, elif, else.   elif (else if, forma abreviada)
# Operadores relacionais ==, <, >, <=, >=, !=
# operadores lógicos or, and, not, in, not in

studant = input('Whats your name? ')
n1 = float(input('Tell your first note: '))
n2 = float(input('Tell your second note: '))
m = float(n1+n2)/2

if (m == 7):
     print ('APPROVED ON AVERAGE *********')
     print (f'First note was: {n1} \ nYour second note was: {n2} ')
     print (f'dear student {studant} your average was {m}')
elif (m> 7 and m <10):
     print ('APPROVED *********')
     print (f'First note was: {n1} \ nYour second note was: {n2} ')
     print (f'dear student {studant} your average was {m} ')
elif (m == 10):
     print ('DRAW DEIZAOOO !! *********')
     print (f'First note was: {n1} \ nYour second note was: {n2} ')
     print (f'dear student {studant} your average was {m}')
elif (m> 0 and m <7):
     print ('FAILED !! *********')
     print (f'First note was: {n1} \ nYour second note was: {n2} ')
     print (f'dear student {studant} your average was {m} ')
elif (m == 0):
     print ('YOU ARE CHIPPED !! *********')
     print (f'First note was: {n1} \ nYour second note was: {n2} ')
     print (f'dear student {studant} your average was {m} ')

a = ''
if not a:  #senão é verdadeiro
    print('preencha o valor')

nome = 'josue'

if 'u' in nome:  # se existe a letra u no valor da variável
    print('existe u em seu nome')

if 'su' not in nome:  # se não existe as letras su no valor da variável
    print('não existe')