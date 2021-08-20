preço = float(input('Qual o preço do produto? R$'))
desconto = float(input('Qual o valor do desconto %?'))
result = preço - (preço*desconto/100)
print('O Produto que custava {}R$, Com desconto de {}% fica {}R$'.format(preço,desconto,result))