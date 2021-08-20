from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento? '))
idade = atual-nasc
print(f'Você nasceu em {nasc} e tem {idade} em {atual}')
if idade == 18:
    print('precisa se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'faltam {saldo} anos para o alistamento')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos. ')
