#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('Escreva um número: '))
res = trunc(num)

print ('O número {} e a sua porção inteira é {}'.format(num, res))