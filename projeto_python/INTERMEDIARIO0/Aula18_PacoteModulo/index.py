from vendas.calc_preco import calc_preco
import vendas.formata.preco as formata

v = calc_preco("josue", 50.76546, True)

print(v)


preco = 55.4555
print(formata.real(preco))




