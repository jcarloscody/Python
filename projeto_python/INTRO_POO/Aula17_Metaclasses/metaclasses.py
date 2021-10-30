"""EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()



class B(A):
    pass


b = B()