#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

n = int(input('Escreva um valor:'))

d = n*2
t = n*3
rq = n**(1/2)

print('O dobro de {} é {}'.format(n, d))
print('O triplo é {}'.format(t))
print('A raiz quadrada é {:.2f}'.format(rq))