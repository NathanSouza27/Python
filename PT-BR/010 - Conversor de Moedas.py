#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode 
#comprar. Considere 1U$ = R$ 3,27.

mon = float(input('Quanto dinheiro você tem em sua carteira? U$ '))

con = mon * 3.27

print('Com U$ {} voce pode comprar R$ {:.2f}'.format(mon, con))