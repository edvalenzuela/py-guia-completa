
listaCompra = ['manzana', 'peras', 'platanos', 1, False, 1.0, True, 'lejia', 'pipas']

empty_list = []

listaConOtraLista=['string', 0, listaCompra]
# get
print(listaConOtraLista[2][2])

# editar
listaCompra[7]= 'lavavajillas'
print(listaCompra[7])

# eliminar
listaCompra.remove('platanos')

# añadir
listaCompra.append('platanos de canarias')

# insert
listaCompra.insert(2, 'platanos de canarias2')
print(listaCompra)

# tamaño de la lista
print(len(listaCompra))

# index
print(listaCompra.index('platanos de canarias2'))

lista = [1, 2, 3]
lista2 = [1, 2, 3, 1, 1, 1]
# max
print(max(lista))

# min
print(min(lista))

# count
print(lista2.count(1))

# reverse
listaCompra.reverse()
print(listaCompra)

# operaciones
print(lista * 3)

# ciclos
print('pipas' in listaCompra)
