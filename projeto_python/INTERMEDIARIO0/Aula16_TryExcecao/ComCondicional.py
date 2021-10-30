def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except:
            pass   #com o pass então por padrão todo try retorna none

numero = converte_numero(input("digite um numero"))

if numero is not None:
    print(numero+100)
else:
    print("digite um numeor valido")
