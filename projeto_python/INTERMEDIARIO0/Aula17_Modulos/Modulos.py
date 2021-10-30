"""MODULOS PADRAO Do python
modulos sao arquivos .py (que contem codigo puthon) e servem para expandir
as funcionalidades padrao da linguagem
docs.python.org/3/py-modindex.html"""

from sys import platform as plataformadopc
from sys import platform
import sys

#instalar modulo. pelo terminal::::   pip install nome_modulo  //// pip uninstall nome_module

print(plataformadopc)
print(platform)
print(sys.platform)

#sobrescreveu CUIDADO
def platform():
    return "moism"


print(platform())