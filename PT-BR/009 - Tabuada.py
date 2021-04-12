#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Escreva um número: '))

tab1 = num * 1
tab2 = num * 2
tab3 = num * 3
tab4 = num * 4
tab5 = num * 5
tab6 = num * 6
tab7 = num * 7
tab8 = num * 8
tab9 = num * 9

print('-' * 12)
print('{} x 1 = {}'.format(num, tab1))
print('{} x 2 = {}'.format(num, tab2))
print('{} x 3 = {}'.format(num, tab3))
print('{} x 4 = {}'.format(num, tab4))
print('{} x 5 = {}'.format(num, tab5))
print('{} x 6 = {}'.format(num, tab6))
print('{} x 7 = {}'.format(num, tab7))
print('{} x 8 = {}'.format(num, tab8))
print('{} x 9 = {}'.format(num, tab9))
print('-' * 12)