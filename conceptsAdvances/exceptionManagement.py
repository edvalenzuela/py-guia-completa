
# manejando una excepción

try:
  print(x)
except:
  print('Excepcion debidoa que no hemos inicializado la x')
  x = 1 

# manejando más de una excepción

try:
  print(y)
except NameError:
  print('NameError')
except:
  print('Es otro tipo de error') 

try:
  f=open('fileExample.txt', 'r')
  f.write('La vida es, es un instante de maravilla')
except:
  print('no se ha podido escribir el fichero')
finally:
  f.close()
  print('cerrando fichero')
  
num = -2

if num < 0:
  raise Exception('Error producido cerrando programa')