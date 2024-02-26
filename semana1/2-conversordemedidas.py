medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida *10
km = medida /1000


print('A medida de {}m corresponde a:\n{:.0f}cm \n{:.0f}mm \n{:.0f}dam \n{:.0f}km '.format(medida, cm, mm, dam, km))