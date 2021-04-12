#Make a program that reads the names of four students and shows the order drawn for the presentation.

import random

pa = str(input('First student: '))
sa = str(input('Sencond student: '))
ta = str(input('Third Student: '))
qa = str(input('Fourth student: '))
lista = [pa,sa,ta,qa]

random.shuffle(lista)

print('The order will be {}'.format(lista))

