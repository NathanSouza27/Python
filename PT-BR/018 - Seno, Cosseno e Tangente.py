# Faça um programa que leia um ângulo qualquer e mostre na tela o calor do seno,cosseno e tangente desse ângulo.

import math

ang = float(input('Insira o ângulo que você deseja: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo de {} tem o seno {:.2F}'.format(ang,sen))
print('O ângulo de {} tem o cosseno {:.2F}'.format(ang,cos))
print('O ângulo de {} tem a tangente {:.2F}'.format(ang,tan))