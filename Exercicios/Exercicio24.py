numero = int(input('Digite um número qualquer: '))
print(''' Escolha uma das bases de converção:
[1] Converter para Binario
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua Opção: '))

if opcao == 1:
    print('{} Convertido para Binário é igual a:{} '.format(numero,bin(numero)))
elif opcao == 2:
    print('{} Convertido para Octal é igual a: {}'.format(numero,oct(numero)))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a: {}'.format(numero,hex(numero)))
else:
    print('Número inválido!')
