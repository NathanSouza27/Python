#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Escreva um valor:'))

a = n - 1
s = n + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(n, a, s))