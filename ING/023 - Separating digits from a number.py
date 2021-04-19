#Make a program that reads numbers from 0 to 9999 and shows each separate digit on the screen

num = int(input('Enter a number from 0 to 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analyzing the number {}'.format(num))
print('Units: {}'.format(u))
print('Dozens: {}'.format(d))
print('Hundreds: {}'.format(c))
print('Thousand: {}'.format(m))