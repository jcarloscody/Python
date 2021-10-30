'''
/
*
+
-
** exponenciação
// Esta é uma divisão inteira
%
()
PRECEDÊNCIA
1 - ()
2 - **
3 - /, *, // , %
4 - +, -
https://docs.python.org/3/reference/expressions.html#operator-precedence
'''

print('soma +', 10+10)
print('multiplicação *', 10*10)
print('divisão 3/10', 3/10)
print('divisão inteira 3//10', 3//10)
print('subtração -', 10-10)
print('potenciação 10**10', 10**10)
print('resto de divisão 10%10', 10%10)
print('resto de divisão 4%3', 4%3)

print("multiplicação 10*'josué'", 10*'josué')  #repetição
print('concatenação +', 'carlos' + ' ' + 'josué' + str(9))  #concatenação, só pode com o mesmo type. str () convertendo
# um número em str. apenas para conhecimento. DEVEMOS TER CÓDIGO LIMPO



