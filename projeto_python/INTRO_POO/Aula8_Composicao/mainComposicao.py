from ClassesComposicao import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()


cliente2 = Cliente('Maria', 32)
cliente2.insere_endereco('São Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()


cliente3 = Cliente('Joao', 32)
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
print()


print()
print()
print("@@@@@@@@@@@@@")
print()


