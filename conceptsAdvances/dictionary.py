# nombre_dictionary + { "clave": valor, "clave": valor}
# es posible encadenar diccionarios

carBmw = { "brand": "bmw", "potencia": 158, "precio": 34000 }
carPorsche = { "brand": "porsche", "potencia": 215, "precio": 48000 }

carsToBuy = {"coches": [carBmw, carPorsche]}

# acceso al dato
print(carsToBuy["coches"])
print(carBmw["brand"])
print("=======")

# accede a los valores
for value in carBmw.values():
  print(value)
print("=======") 

# accede a la clave
for key in carBmw.keys():
  print(key)
print("=======")

# acceder a la clave valor indistintamente
for itemKey, itemValue in carBmw.items():
  print(itemKey, itemValue)
print("=======")   

# modificacion del dato
carBmw["brand"] = "ferrari"

# añadir nuevo elemento
carBmw["nuevo"] =  True
print(carBmw)

# borrar key, se puede utilizar del o pop de la misma forma
del carBmw["brand"]
carBmw.pop("potencia")
print(carBmw)

# limpiar diccionario
carBmw.clear()
print(carBmw)