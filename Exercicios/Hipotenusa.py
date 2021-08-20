co = float(input('Cateto oposto? '))
ca = float(input('Cateto adjacente? '))
hipo = (ca ** 2 + co ** 2) ** (1/2)
print ('A Hipotenusa é {:.2f}'.format(hipo))

#Ou

import math
co = float(input('Cateto oposto? '))
ca = float(input('Cateto adjacente? '))
hipo = math.hypot(co,ca)
print ('A Hipotenusa é {:.2f}'.format(hipo))

