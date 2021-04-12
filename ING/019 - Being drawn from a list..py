#A teacher wants to raffle one of his four students to erase the board. Make a program that helps him, reading their
# names and writing the name of the chosen one.

import random

pa = str(input('First student: '))
sa = str(input('Sencond student: '))
ta = str(input('Third Student: '))
qa = str(input('Fourth student: '))

lista = [pa,sa,ta,qa]
res = random.choice(lista)

print('{}'.format(res))

