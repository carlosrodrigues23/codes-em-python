# programas-em-python

print('+'*20)
print('Calcule seu IMC')
print('+'*20)

nome = input('Digite o seu nome:\n')
altura = input('Digite a sua altura: ex(1.80)\n ')
peso = input('Digite o seu peso: ex(75.0)\n')

float_altura = float(altura)
float_peso = float(peso)

IMC = float_peso/(float_altura*float_altura )

print(f'Oi {nome}, seu IMC eh:\n {IMC:.2F}')