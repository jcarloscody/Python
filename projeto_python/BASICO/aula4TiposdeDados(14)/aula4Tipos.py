"""
Tipos de Dados
str - String - texto
int - inteiro
float - flutuante - 2.5, 3.8
bool - boleano /lógico true,false
"""

print('josué', type('Josué'))  #a classe type vai retornar o tipo. por isso os parênteses.

print(10, type(10))
print(-11, type(-11))
print(2.3, type(2.3))
print('l'=='L', type('l'=='L'))

print(bool(1.0))  # aqui é true, pois tem valor

print(bool(0.0))  # aqui é false, pois é vazio


print('10', type('10'), type(int('10')))  # converteu o string em int. nem sempre é possível converter um texto em
# inteiro. como por ex converter 'Luiz' em inteiro, impossível ou float 1.2 em inteiro, impossível, mas é possível int
# em float
