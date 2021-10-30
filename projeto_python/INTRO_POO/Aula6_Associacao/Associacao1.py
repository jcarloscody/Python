class Escritor:
    def __init__(self):
        self.__nome
        self.__ferramenta = None

    @property
    def GetNome(self):
        return self.__nome

    @property
    def Ferramenta(self):
        return self.__ferramenta

    @Ferramenta.setter
    def Ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta





class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def Getmarca(self):
        return self.__marca

    def escreverCaneta(self):
        print('Caneta está escrevendo...')




class MaquinaDeEscrever:
    def escreverMaquina(self):
        print('Caneta está escrevendo...')