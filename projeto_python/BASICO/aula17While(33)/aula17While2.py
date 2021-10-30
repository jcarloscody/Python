contador = 0
while contador <= 2000:
    print(contador)
    contador += +1

contador2 = 0
acumulador = 0
while contador2 <= 20:
    print(contador2, acumulador)
    acumulador += +contador2
    contador2 += +1
else:  #será usado quando o while for false
    print('Cheguei no else')