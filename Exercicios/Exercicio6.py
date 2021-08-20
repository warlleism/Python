real = float(input('Digite seu valor em R$: '))
dolar = real / 5.37
euro = real / 6.38
print('{:.2f}R$ em dolar : {:.2f}US$'.format(real,dolar))
print('{:.2f}R$ em dolar : {:.2f}€$'.format(real,euro))
