#Create an algorithm that reads a number and shows its double, triple and square root.

n = int(input('Type it a value:'))

d = n*2
t = n*3
rq = n**(1/2)

print('The double of {} is {}'.format(n, d))
print('The triple is {}'.format(t))
print('The square root is {:.2f}'.format(rq))