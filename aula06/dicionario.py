#no dicionario voce cria a CHAVE E O VALOR


livro = {'autor': 'Ze', 'titulo': 'Aventuras de programação', 'paginas': 300}

print(livro)

livro2 = livro = {'autor': 'João', 'titulo': 'Java para iniciante', 'paginas': 10000}

biblioteca = {'livros': [livro, livro2], 'endereco': 'Praça XV'}

print(biblioteca)

#biblioteca[0] não existe o indice 0, mas sim a chave livros e endereco

print(biblioteca['livros'])

print(biblioteca['endereco'])

#desta forma ele inseri, com o atributo INSERT não conseguimos
livro['data_lancamento'] = '22/01/2018'

print(livro)

#livro2.insert('data_lancamento': '02/01/2010') desta forma não funciona

livro2['autor'] = 'João Paulo'

print(livro2)

bebidas = {'Cerveja': 'Original', 'Refrigerante': 'Coca-cola'}

print(bebidas)

Refrigerante = ['Coca-cola', 'Sprit']

print(Refrigerante)

Hortifrutti = ['Alface', 'Cebola', 'Cenoura']

Compras = [Refrigerante+Hortifrutti]

print(Compras)

Cerveja = ['Original', 'Opa', 'Heineken']

bebidasnova = [[Refrigerante]+[Cerveja]]

print(bebidasnova)