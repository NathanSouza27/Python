# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,calcule e
# mostre o comprimento da hipotenusa.

import math

ca = float(input('Comprimento do cateto oposto: '))
cb = float(input('Comprimento do cateto adjacente: '))

h2 = math.hypot(ca,cb)

print('A hipotenusa irá medir {:.2f}'.format(h2))