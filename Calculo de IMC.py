# programas-em-python

print('+'*20)
print('Calcule seu IMC')
print('+'*20)

nome = input('Digite o seu nome:\n')
altura = input('Digite a sua altura: ex(1.80)\n ')
peso = input('Digite o seu peso: ex(75.0)\n')

float_altura = float(altura)
float_peso = float(peso)

IMC = float_peso/(float_altura*float_altura)

print(f'Oi {nome}, seu IMC eh:\n {IMC:.2F}')

if IMC <18.5:
  print('você está magro')

elif IMC >=18.5 and IMC <=24.9:
  print('você está com peso normal')

else:
  print('você está com sobrepeso')
