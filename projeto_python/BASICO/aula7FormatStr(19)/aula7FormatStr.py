nome = 'josué'
idade = 32
altura = 1.2
e_maior = idade > 18
peso = 71
imc = peso / (altura**altura)

print(nome, 'tem ',idade, ' anos de idade e seu IMC é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc}')
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é: {2:.2f}. \nDessa forma, {0},{1},{2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é: {im:.2f}. '.format(n=nome, i=idade, im=imc))

