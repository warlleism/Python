import random
n1 = str(input('Primeiro aluno '))
n2 = str(input('Primeiro segundo '))
n3 = str(input('Primeiro terceiro '))
n4 = str(input('Primeiro quarto '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))