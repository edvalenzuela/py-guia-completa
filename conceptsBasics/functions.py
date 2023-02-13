
itemsAvailableList = ['tu puedes con todo', 'aprenderas', 'pentesting web', 'y ethical hacking']

def welcomeMessage():
  print('Bienvenido a shopping market, cargando información...')
  print('Por favor, introduzca su nombre de usuario: ')

def requestUsername(username):
  print('Nombre de usuario disponible, '+username)

def isAvailable(item):
  return item in itemsAvailableList

# main
welcomeMessage()
userName = input()
requestUsername(userName)

print('Por favor introduzca el producto que desea comprobar: ')
userBuy = input()
print(isAvailable(userBuy))


  