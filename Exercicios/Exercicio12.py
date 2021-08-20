import math
angulo = int(input('Digite o ângulo que voce deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem SENO de {:.2f} '.format(angulo,sen))
print('O ângulo de {} tem COSSENO de {:.2f} '.format(angulo,cos))
print('O ângulo de {} tem TANGENTE de {:.2f} '.format(angulo,tan))

#Ou

from math import radians,sin,cos,tan
angulo = int(input('Digite o ângulo que voce deseja: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {} tem SENO de {:.2f} '.format(angulo,sen))
print('O ângulo de {} tem COSSENO de {:.2f} '.format(angulo,cos))
print('O ângulo de {} tem TANGENTE de {:.2f} '.format(angulo,tan))