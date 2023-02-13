
print('¿Quieres acabar con el mundo?\n')

# .- Sentencias if
inputUser = input()
if inputUser == 'yes' or inputUser == 'y':
  print('Lanzando misil...')
elif inputUser == 'no' or inputUser == 'n':
  print('Cancelando el lanzamiento')
  
# .- for loops
listaCompra = ['manzanas', 'peras', 'platanos']
for i in listaCompra:
  print(i+'\n')
  
# .- while loops
count = 1

while count <= 10:
  print(count)
  count+=1
print('se ha acabado')

# .- switch
diaElegido = int(input())

if diaElegido == 1:
  print('Lunes')
elif diaElegido == 2:
  print('Martes')
else:
  print('No existe')