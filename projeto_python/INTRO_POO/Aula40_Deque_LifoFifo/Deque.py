"""Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    exemplo: pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: uma fila de banco (ou qq fila da vida real)
FILAS podem ter efeitos colaterais em desempenho, porque a cada item alterado,
todos os índices serão modificados.
"""

from collections import deque   #para criar uma lista do tipo fila

 #PILHA
livros = list()

livros.append('livro1')
livros.append('livro3')
livros.append('livro2')
print('livros: ',livros)

livros_removido = list()
livros_removido.append(livros.pop()) #removeu o ultimo e salvou na variável
livros_removido.append(livros.pop())

print('livros: ',livros)
print('livros_removido: ',livros_removido)

print()


#FILA
fila = deque()
fila2 = deque(maxlen=2 ) #aguenta só 2 valores, se adionar mais, o primeiro valor vaza

print('FILA 1')
fila.append('josue')
fila.append('silva')
fila.append('pica pau')
print('itens[0]-[2]: ', fila[0],fila[1],fila[2])

fila_removido = list()
fila_removido.append(fila.popleft())   #sai o primeiro
fila_removido.append(fila.popleft())
print('itens[0]: ', fila[0])

print()
print('FILA 2')
fila2.append('josue')
fila2.append('silva')
print('fila2: ', fila2)
print('adicionando mais um elemento...')
fila2.append('carlos')
print(fila2)

fila.insert(2,'inserindo na posicao 2')
#print(fila.index(3))
fila.reverse()
print(fila)
fila.reverse()
print(fila)

