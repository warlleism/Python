from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400: #números divisiveis por 4 com resto zero é bissesto
    print('O ano {} é bissesto'.format(ano))
else:
    print('O ano {} não é bissesto'.format(ano))