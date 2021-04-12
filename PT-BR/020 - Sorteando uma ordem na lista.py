# Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada para a aparesentação.

import random

pa = str(input('Primeiro aluno: '))
sa = str(input('Segundo aluno: '))
ta = str(input('Terceiro aluno: '))
qa = str(input('Quarto aluno: '))
lista = [pa,sa,ta,qa]

random.shuffle(lista)

print('A ordem será {}'.format(lista))

