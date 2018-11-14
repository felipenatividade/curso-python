import string

lista = [1,2,3,4,5,6,7,8,9,10]
print(len(lista))
print(min(lista))

del lista[0]
print(lista)

lista2 = range(10)
print(lista2)
print(lista2[9])

#pop(lista2)

#list(lista2).pop()

lista_nova = [1,2,3,4]
print(lista_nova)

lista_nova.append(5)
print(lista_nova)

lista_nova.insert(3, 10)
print(lista_nova)

lista_nova.remove(10)
print(lista_nova)

lista_nova.clear()
print(lista_nova)

lista_nova = [1, 2, 3, 4]

lista_nova.count(2)
print(lista_nova)


print(lista_nova.count(2))

lista_nova.append(2)

print(lista_nova.count(2))

lista_nova.sort()
print(lista_nova)

lista_nova.sort(reverse=True)
print(lista_nova)

lista_nova.index(2, 2)
print(lista_nova)

lista_nova.reverse()
print(lista_nova)


lista_nova.append(None)
lista_nova.append('Z')
lista_nova.append('z')
print(lista_nova)

#lista_nova.sort() não posso colocar em ordem pois uma posição não pode ser NONE, e tbm nem STR, a lista tem que ser do mesmo tipo
lista_nova.remove(None)
lista_nova.reverse()
print(lista_nova)

print(lista_nova[3:])
print(lista_nova[3:4])
print(lista_nova[3:5])
print(lista_nova[::2])
print(lista_nova[:2])
print(lista_nova[::3])
print(lista_nova[:-1])

nome = 'Felipe Rodrigues de Lima Natividade'
print(len(nome))
print(nome[:6])
print(nome[::3])

lista1 = [1, 2, 3, 4, 5]
lista2 = [100, 200, 300]
lista3 = lista1[:3] + lista2
print(lista3)


matriz = [[1,2],[2,4]]
print(matriz)
#print(matriz[0][0])

#matriz = [[1,2],[2,4]]

#print(matriz)

#for index, valor in enumerate(matriz):
#	for i, numero in enumerate(valor):
#		matriz[index][i] = numero**2

#lista dento de lista, podemos utilizar a LIST COMPREHENSIONS
matriz = [[value**2 for value in line] for line in matriz]
print(matriz)


#List Comprehensions

#squares = [x**2 for x in range(10)]
#print(squares)


lista = [1, 2, 3, 4, 5, 6]
[value*10 if value > 3 else value**2 for value in lista]
print(lista)

string.ascii_lowercase
print(list(string.ascii_lowercase))
print(len(list(string.ascii_lowercase)))



novo = range(50)
print(novo)