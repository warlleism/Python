import math

x1 = int(input('Coloque o valor de x1: '))
x2 = int(input('Coloque o valor de x2: '))
y1 = int(input('Coloque o valor de y1: '))
y2 = int(input('Coloque o valor de y2: '))
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)#Tudo que esta aqui dentro sera tirado a raiz quadrada
print('A distância entre os pontos é {:.2f}'.format(d))

#Ou

x1 = int(input('Coloque o valor de x1: '))
x2 = int(input('Coloque o valor de x2: '))
y1 = int(input('Coloque o valor de y1: '))
y2 = int(input('Coloque o valor de y2: '))
dis = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
print('A distância entre os pontos é {:.2f}'.format(dis))