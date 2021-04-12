#Write a program that converts a entered temperature to ° C and converts to ° F.s

temp1 = float(input('Irform a the temperature in °C: '))

temp2 = (temp1 * 9) / 5 + 32

print('The temperature of {}°C stands for {}°F!'.format(temp1, temp2))