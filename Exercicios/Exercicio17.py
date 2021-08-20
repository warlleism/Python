dist = float(input('Distância da viagem em KM: '))
preco1 = (0.50 * dist)
preco2 = (0.45 *dist)
if dist <= 200:
    print('Em uma viagem de {:.2f}KM o custo fica em: R${:.2f}'.format(dist,preco1))
else:
    print('Em uma viagem de {:.2f}KM o custo fica em: R${:.2f}'.format(dist,preco2))