largura = float(input('Largura da sua parede: '))
altura = float(input('Altura da sua aprede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem dimensão {:.0f}x{:.0f} e sua área é de {:.0f}m².'.format(largura,altura,area))
print('Para pintar essa parede, será necessário {:.0f}L de tinta.'.format(tinta))