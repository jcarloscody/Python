class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_endereco(self, cidade, uf):
        self.endereco.append(Endereco(cidade, uf))   #isso transforma a class cliente proprietaria de endereco.

    def lista_enderecos(self):
        for endereco in self.endereco:
            print(endereco.cidade,'|',endereco.uf)

    def __del__(self):
        print(f'o objeto {self.nome} foi apagado')



class Endereco:
    def __init__(self, cidade, uf):
        self.cidade = cidade
        self.uf = uf

    def __del__(self):
        print(f'o obejto {self.cidade}{self.uf} foram apagados')