index = 0                                      
ALUNOS = 5                                    
while index < ALUNOS:
  aop1[index] = float(input(f'Nota [0.0, 1.0] do Aluno {index + 1}:  '))
  if aop1[index] < 0.0 or aop1[index] > 1.0:
    print('Erro na digitação da nota AOP1 [0.0, 1.0]. Escolha de novo.')
  else:
    index += 1
