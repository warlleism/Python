preco = float(input('Preço do produto: '))
quantidade = float(input('Quantidade de produtos: '))
total = quantidade * preco
desconto = total - (total*3/100) 
if total >= 1000:
    print('O preço é {:.0f}R$ e com desconto fica: {:.0f}R$'.format(total,desconto))
else: 
    print('Esse é o valor a pagar: {:.0f}R$'.format(total))
      

