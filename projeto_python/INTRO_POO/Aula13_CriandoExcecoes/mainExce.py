class TaErrado(Exception):
    pass




def testa():
    try:
        x == y
    except:
        raise TaErrado('muitoo errado')





try:
    testa()
except TaErrado as erro:
    print(erro)

print()
print()

testa()