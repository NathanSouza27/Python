#Write a program that reads a value in meters and displays it converted to centimeters to millimeters.

n1 = int(input('A distance in meters'))

km = n1 /1000
hm = n1 /100
dam = n1 / 10 
dm = n1 *10
cm = n1 *100
mm = n1 *1000

print('{} Km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{} dm'.format(dm))
print('{} cm'.format(cm))
print('{} mm'.format(mm))