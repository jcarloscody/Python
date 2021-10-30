from Associacao1 import Escritor
from Associacao1 import Caneta
from Associacao1 import MaquinaDeEscrever

escritor = Escritor('joaozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.Ferramenta = caneta
escritor.Ferramenta.escreverCaneta()

del escritor

print(caneta.marca)
maquina.escreverMaquina()






