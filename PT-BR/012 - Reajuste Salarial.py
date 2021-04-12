#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento..

sal = float(input('Qual é o salário do funcionários? U$ '))

aum = sal * 0.15
total = sal + aum 

print('Um funcionário que ganhou {}, com 15% de aumento, passa a receber U$ {:.2f}'.format(sal, total))