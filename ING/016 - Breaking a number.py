#Create a program that reads any real number from the keyboard and shows its entire portion on the screen.

from math import trunc

num = float(input('Type a number: '))
res = trunc(num)

print ('The number {} is whole part {}'.format(num, res))