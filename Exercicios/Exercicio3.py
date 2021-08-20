n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1**(1/2)
print('Dobro = {}\nTriplo = {}\nRaiz = {:.3}'.format(dobro,triplo,raiz))



#Média

notaMat = float(input('Digite sua nota: '))
notaPort = float(input('Digite sua nota: '))
notaBio = float(input('Digite sua nota: '))
notaHist = float(input('Digite sua nota: '))
notaGeo = float(input('Digite sua nota: '))
soma = (notaBio + notaGeo + notaHist + notaPort + notaMat) /5
print('Sua média é: {:.3f}'.format(soma))
