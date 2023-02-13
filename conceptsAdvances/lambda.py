
# estructura -> lambda parametros: sentencia
# ejemplo 1
res = lambda firstParam, secParam : firstParam * secParam

""" def res(firstParam, secParam):
  return firstParam * secParam """
  
print(res(9, 9))

# ejemplo 2
def funclambda(text):
  return lambda param: param + text

res2 = funclambda('Python !!!')
print(res2('Aprendiendo ...'))