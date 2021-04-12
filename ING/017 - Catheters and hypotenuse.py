#Make a program that reads the length of the opposite leg and the adjacent leg of a right triangle, calculate and show
# the length of the hypotenuse.

import math

ca = float(input('Opposite side length: '))
cb = float(input('Adjacent side lenght: '))

h2 = math.hypot(ca,cb)

print('The hypotenuse will measure {:.2f}'.format(h2))