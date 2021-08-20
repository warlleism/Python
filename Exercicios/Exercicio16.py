numero = int(input('Digite um número: '))
resto = numero % 2
if resto == 0: #numeros com resto na divisão por 2 igual a zero são par.
    print('O número é Par')
else:
    print('O número é Impar')