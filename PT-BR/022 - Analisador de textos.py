#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas e minusculas
#Quantas letras ao todo (sem considera os espaços).
#Quantas letras tem o primeiro nome
nome = input('Qual o seu nome? ')

print('Tudo maiúsculo: {}'.format(nome.upper()))

print('Tudo minúsculo: {}'.format(nome.lower()))

lista = nome.split()

print('O nome completo possui {} letras'.format(len(''.join(lista))))

print('O seu primeiro nome é {} e possui {} letras'.format(lista[0], len(lista[0])))
