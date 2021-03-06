
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome;
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            v = valor.upper();
            valor = float(v.replace('R$', ""))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()



p1 = Produto('camisa', 'r$100')
p1.desconto(50)
print( p1.nome,p1.preco)

