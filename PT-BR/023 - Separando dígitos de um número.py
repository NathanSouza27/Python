#Faça um programa que leia número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero {}'.format(num))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))