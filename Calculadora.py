x = float(input('digite o numero:\n'))
z = float(input('digite o numero:\n'))
print('\n')
op = float(input('\n\n1 para somar\n2 para subtrair\n3 para multiplicar\n4 para dividir\n '))

match op:
    case 1:
      soma = x + z 
      print(f'a soma eh:\n {soma}')
    case 2:
      subtrair = x - z
      print(f'a subtraçao eh:\n {subtrair}')
    case 3:
      multiplicar = x * z
      print(f'a multiplicaçao eh:\n {multiplicar}')
    case 4:
      dividir = x / z
      print(f'a divisao eh:\n {dividir}')
