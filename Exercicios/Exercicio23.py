valor = float(input('Qual o valor da Casa?:R$'))
salario = float(input('Salário do comprador:R$'))
parcelamento = int(input('Deseja parcelar em quantas vezes?:R$'))
parcelamentoPorMes = valor / parcelamento
porcentagem = salario * 30/100

if parcelamentoPorMes <= porcentagem:
    print('Orçamento acima do possível. Emprestimo negado!')
else:
    print('Emprestimo Aprovado! Faça um bom negócio')


#OU

valor = float(input('Qual o valor da Casa?:R$'))
salario = float(input('Salário do comprador:R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = valor / (anos * 12)#Anos que quer pagar e a quantidade de meses resultado = qts meses ele paga
minimo = salario * 30/100

if  prestacao <= minimo:
    print('Emprestimo Aprovado! Faça um bom negócio')
else:
    print('Orçamento acima do possível. Emprestimo negado!')



