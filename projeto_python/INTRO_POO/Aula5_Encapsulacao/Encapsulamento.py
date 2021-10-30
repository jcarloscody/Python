"""
public protected private  - o py não usa essa lavrinhas, em vez disso temos convenções como
_   private
__  protected
como é uma converção entao não é obrigatório, porém o dev deve respeitar. os dev de py são adultos e vacinados,
se há _ __ o dev deve respeitar como private ou protected


"""

class BaseDeDados:
    def __init__(self):
        self._dados = {}


    @property   #isso daqui vai dar acesso ao atributo por convenção protegido
    def dados(self):
        return self._dados

    def inserirCliente(self, id, nome):
        if 'cliente' not in self._dados:
            self._dados['cliente'] = {id:nome}
        else:
            self._dados['cliente'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self._dados['cliente'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['cliente'][id]
         # self.dados['cliente'].pop(id)


db = BaseDeDados()
"""
db.inserirCliente(1,'josue')
db.inserirCliente(2,'wanderson')
db.lista_clientes()
db.inserirCliente(2,'carlos')
db.inserirCliente(3,'carlos')
db.inserirCliente(4,'carlos')
db.lista_clientes()
db.apaga_cliente(4)
db.lista_clientes()
"""
#db._dados= ''   #nao deve fazer isto

