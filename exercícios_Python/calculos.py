n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
soma, sub, div, mult,exp = [n1 + n2, n1 - n2, n1 / n2, n1 * n2, n1 ** n2]
print('A soma dos valores são: {}\n'.format(soma) +
      'A subtração dos valores são: {}\n'.format(sub) +
      'A divisão dos valores são: {}\n'.format(div) +
      'A multiplicação dos valores são: {}\n'.format(mult) +
      '{} elevado a {} é igual a: {}\n'.format(n1, n2, exp))
