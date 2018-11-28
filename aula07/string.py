texto = "12345"
print(texto)

#a String tem funções constantes

print("Felipe".isalpha())
print('1234'.isdigit())
print('08388429922'.isdigit())
print('Felipe Natividade'.startswith('Fe'))
print('Felipe Natividade'.endswith('de'))
print('Felipe Natividade'.find('at'))
print('Felipe Natividade'.replace('Fe', 'Su'))
print('00011122334445555'.replace('0', '6'))
print('Felipe Natividade'.replace('Fe', ''))
print(''.join(['a', 'b', 'c']))
print(' '.join(['a', 'b', 'c']))
print('1'.join(['a', 'b', 'c']))


print('{0}, {1}, {2}'.format('a', 'b', 'c'))