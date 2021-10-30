estudante = input('Digite o seu nome: ')
nota1 = float(input('Digite a sua primeira nota: '))  #devemos fazer um type cast (conversão de tipo) aqui,
# pois todo input é str

nota2 = float(input('Digite a sua segunda nota: '))
media = float(nota1+nota2)/2
print(f'caro aluno {estudante} a sua media foi {media}')
