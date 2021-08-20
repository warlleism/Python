quilo = int(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = quilo / (altura**2)
print('Seu IMC é = {:.2f}'.format(imc))