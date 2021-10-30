from Eletronico import *
from log import *


class smartphone (Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} ñ está ligado'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            info = f'{self._nome} já está conecatado'
            self.log_error(info)
            return

        info = f'{self._nome}  está conecatado'
        print(info)
        self.log_info(info)
        self._conectado = True


    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} ñ está conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desligado'
        print(info)
        self.log_info(info)
        self._conectado=False
