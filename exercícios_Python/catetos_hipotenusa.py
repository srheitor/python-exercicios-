co = float(input('Digite um valor'))
ca = float(input('Outro valor'))

hi = (co**2 + ca**2) ** (1/2)

print('A hipotenusa irá medir: {:.2f}'.format(hi))

import math
co = float(input('Digite um valor'))
ca = float(input('Outro valor'))
hi = math.hypot(co, ca)

print('A hipotenusa irá medir: {:.2f}'.format(hi))