class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        return f'{self.nome_classe} falando'

    def falar2(self):
        print(f'{self.nome_classe} está falanod')


class Cliente(pessoa):
    def comprar(self):
        print(f'{self.nome_classe} comprando...')


class Aluno(pessoa):
    def estudar(self):
        print(f'{self.nome_classe} estudando...')

    def falar(self):
        print('Estou em cliente')



#sobreposição de membros
class ClienteVIP(Cliente):
    def falar(self):
        #super().falar() #neste caso vai da superclasse cliente e não pessoa
        super().falar2()     #está se referindo a super classe. neste caso é da classe pessoa. se o método estivesse na classe cliente, então o super iria indicar a classe cliente
        return f'{self.nome_classe} está faladnod'



class ClienteVIPE(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome,idade)
        self.sobrenome = sobrenome

    def falar(self):
        pessoa.falar(self)
