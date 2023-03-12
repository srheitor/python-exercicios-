b = float(input('Digite a Largura da parede: '))
h = float(input('Digite a Altura da parede: '))
a = b * h

print('A área da parede é de: {}'.format(a), 'm²')
lata = 2
quant_lata = (a/lata)

print('Será nescessário para pintar esta parede {}'.format(quant_lata), 'litros de tinta')