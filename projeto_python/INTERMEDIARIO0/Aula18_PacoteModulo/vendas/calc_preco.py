from INTERMEDIARIO.vendas.formata import preco


def calc_preco(nome, valor, formata=False):
    print(nome)
    if formata==True:
        return preco.real(valor)
    else:
        return valor


