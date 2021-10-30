import  random


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):    #o self se refere a própria instancia
        print(self.ano_atual - self.idade)

    #issso se chama decorador
    @classmethod   #metodo de classe. não precisa de self, pois se refere a classe e não ao objeto
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        print(idade)



    @staticmethod  #é um método que não precisa de instancia (self) nem da classe. é um função
    #indepente que por organização fica dentro da classe.
    def gera_id():
        rand = random.randint(10000, 19999)
        return rand


p1 = Pessoa
p1.por_ano_nascimento('jos',1999)

print(p1.gera_id())  #apesar de ser static pode ser chamado pelo objeto
print(Pessoa.gera_id())

