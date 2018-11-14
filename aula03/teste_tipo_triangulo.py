a, b, c

def dado_do_usuario():
	input("Digite um numero")



a = input("Digite a primeira medida")
b = input("Digite a segunda medida")
c = input("Digite a terceira medida")

if (a+b<c) or (a+c<b) or (b+c<a):
	    print('Nao é um triangulo')
elif a==b and a==c:
	    print('Equilatero')
elif (a+b!=c)  or (a+c!=b) or (b+c!=a):
	    print('Isósceles')
else:
	    print('Escaleno')

	    print('Você terminou o jogo, PARABÉNS!')