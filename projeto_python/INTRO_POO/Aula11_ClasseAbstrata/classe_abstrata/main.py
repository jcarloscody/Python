from classes.ContaPoupanca import ContaPoupanca
from classes.ContaCorrente import ContaCorrente


ContaPoupanca = ContaPoupanca(1111, 2222, 0)
ContaPoupanca.depositar(10)
ContaPoupanca.sacar(5)
ContaPoupanca.sacar(5)
ContaPoupanca.sacar(1)

print('##########################')
ContaCorrente = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
ContaCorrente.depositar(100)
ContaCorrente.sacar(250)
ContaCorrente.sacar(500)
ContaCorrente.depositar(1000)


