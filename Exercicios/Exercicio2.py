n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1+n2
sub = n1-n2
divi = n1/n2
di = n1//n2
mult = n1*n2
esp = n1**n2
print('soma = {}\n,sub = {}\n,div = {:.3}'.format(soma, sub, divi),end = ' ')
print('di = {}, mult = {}, esp = {}'.format(di,mult, esp))
#{:.3} = para que apareçam apenas 3 números
#end = ' ' para deixar os 2 prints na mesma linha
# " \n " para quebrar a linha
