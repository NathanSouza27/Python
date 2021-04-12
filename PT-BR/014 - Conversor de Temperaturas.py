#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temp1 = float(input('Informe a temperatura em °C: '))

temp2 = (temp1 * 9) / 5 + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(temp1, temp2))