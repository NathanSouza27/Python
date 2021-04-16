#Create a program that reads a person's full name and shows:
#The name with all uppercase and lowercase letters
#How many letters have the first name
name = input('What is your full name? ')

print('All uppercase: {}'.format(name.upper()))

print('All lowercase: {}'.format(name.lower()))

list = name.split()

print('The full name has {} letters'.format(len(''.join(list))))

print('Your first name is {} and has {} letters'.format(list[0], len(list[0])))