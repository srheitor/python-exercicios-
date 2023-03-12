import math

an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print("O ângulo {} tem o SENO de {:.2f}\n".format(an, seno),
      'O ângulo {} tem o COSSENO de {:.2f}\n'.format(an, cosseno),
      'O ângulo {} tem a TANGENTE de {:.2f}'.format(an, tangente));
