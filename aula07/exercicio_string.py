txt1 = input('Digite a primeira frase: ')
txt2 = input('Digite a segunda frase: ')

if txt1 == txt2:
	print('As frases são iguais')
else:
	print('As frases são diferentes')

if len(txt1) == len(txt2):
	print('As duas frases são de tamanhos iguais')
else:
	print('As duas frases são de tamanhos diferentes')

print('A primeira frase tem ' + str(len(txt1)) + ' caractéres')
print('A segunda frase tem ' + str(len(txt2)) + ' caractéres')

