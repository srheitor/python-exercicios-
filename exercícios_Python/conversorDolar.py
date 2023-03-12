quant_dolar = float(input('Digite quantos dolares você deseja: $'))
real = float(5.22)
dolar_real = quant_dolar*real

print('Você deseja ${:.2f} dolares, isso convertido a reais fica em um valor de: R${:.2f} reais'.format(quant_dolar,dolar_real))
