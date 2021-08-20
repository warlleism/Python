import math
num = float(input('Digite um número: '))
porção = math.floor(num)
print('O número {} tem a parte inteira {}'.format(num,porção))

#Ou 

import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num,math.floor(num)))

#Ou (Importando apenas a bibliotéca floor e ceil)

from math import floor
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num,math.floor(num)))

#Ou (Usando "trunc" que elimina os números depois da vírgula)

from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num,math.trunc(num)))

#ou

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num,int(num)))