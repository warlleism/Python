largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))
profundidade = float(input('Qual a profundidade: '))
precoAlcool = float(input('Preço por litros:Álcool (R$ / Litro)'))
precoGasolina = float(input('Preço por litros:Gasolina (R$ / Litro)'))
volume = largura * altura * profundidade * 1000  #esta em metros cubicos ,convertendo pra litros
precoGaso = precoGasolina * volume
precoAlco = precoAlcool * volume
precoAlcoEGaso = 0.2 * volume * precoAlcool + 0.8 *volume * precoGasolina
print('O valor do alcool: R${:.2f}'.format(precoAlco))
print('O valor da gasolina: R${:.2f}'.format(precoGaso))
print('O valor do Alcool e Gasoilna: R${:.2f}'.format(precoAlcoEGaso))
