import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor() #com este cursor iremos executar os comando sql dentro da base de dados

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("josue", 129.5)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("josue", 10)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
               {'nome':'joaozinho', 'peso':25}
               )
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
               {'id': None, 'nome':'Daniel', 'peso':250}
               )
conexao.commit()  #para executar os comandos


#ATUALIZAR DADOS
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome':'joana', 'id':2}
               )
conexao.commit()


#DELETANDO DADOS
cursor.execute('DELETE FROM clientes WHERE id=:id',
               {'id':2}
               )
conexao.commit()


#MOSTRANDO DADOS
"""cursor.execute('SELECT * FROM clientes')

for valor in cursor.fetchall(): #vai trazer todos os valores executados
    id, nome, peso = valor #desapocando
    print('id: ' , id, 'nome: ' ,  nome,'peso: ', peso)
"""
#cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 50})

for valor in cursor.fetchall(): #vai trazer todos os valores executados
    nome, peso = valor #desapocando
    print('nome: ' ,  nome,'peso: ', peso)

cursor.close()
conexao.close()