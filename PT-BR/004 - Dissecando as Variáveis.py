#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações 
#possiveis sobre ele.

n = input('Escreva algo:')

print('O tipo primitivo deste valor é:',type(n))
print('Só tem espaços?',n.isspace())
print('É um número?',n.isnumeric())
print('É alfabético?',n.isalpha())
print('É alfanumérico?',n.isalnum())
print('Está em maiúsculas?',n.isupper())
print('Está em minúsculas?',n.islower())
print('Está capitalizada?',n.istitle())