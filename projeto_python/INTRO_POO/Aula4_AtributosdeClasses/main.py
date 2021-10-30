
class A:
    vc = 123   #isso é atributo da classe e não atributo de instancia


p = A()   #mas pode pegar atributos de classe por meio de instancia
print(p.vc)

print(A.vc)  #pode pegar diretamente pela classe

A.vc = 904

print(p.vc)
p.vc = 123344  #é importante ficar ligado nisto aqui. pq com isso se altera o valor da instanciação, mas não o atributo da classe

print(p.vc, A.vc)
