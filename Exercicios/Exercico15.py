velocidade = float(input('Velocidade do veículo:'))
multa = (velocidade - 80)*7
if velocidade > 80:
    print('Você foi Multado! Sua multa é de: R${:.2f}'.format(multa))  
else:
    print('Você está dentro do limite de velocidade!')

vel = float(input('Velocidade do veículo: '))

soma = (vel - 80)*10
if vel > 80:
    print('Infração! Sua multa é de {:.2f} R$'.format(soma))
else:
    ('Você esta dentro do limite de velocidade')
