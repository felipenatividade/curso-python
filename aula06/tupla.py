#uma tupla é imutável, quando criada não pode ser alterada
# é uma lista de valores separados por virgulas
#quando mexermos com valores fixo usaremos tupla

tupla = (1, 2, 3, 4, 5)
print(tupla[0])

#print(tupla.append(10)) este atributo APPEND nao existe

tupla2 = (6, 7, 8, 9, 10)

print(tupla+tupla2)

#del dupla[0] este atributo nao funciona

#tupla.reverse() este atributo nao funciona, ele permanece na ordem que voce criou

tuplanova = 'a', 'b', 'c', 'd', 'e'

print(tuplanova)

tuplanova1 = 'Felipe', 10, 20

print(tuplanova1)

nome, idade, nascimento = tuplanova1

print(nome)
print(idade)
print(nascimento)