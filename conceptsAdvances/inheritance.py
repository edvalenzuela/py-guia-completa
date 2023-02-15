# herencia clase que hereda propiedades de la clase padre

# clase animal - padre
class Animal:
  food = 50 # 0 esta hambriento y 100 esta no hambriento
  
  def __init__(self, name, age, velocity, acuatic):
    self.name = name
    self.age = age
    self.velocity = velocity
    self.acuatic = acuatic
  
  def __isHungry(self):
    return self.food < 50
  
  def makingHungry(self, food):
    self.food-= food
  
  def eat(self):
    if self.__isHungry():
      self.food+=10
    
  def defend(self):
    print(self.name+' Me estoy defendiendo de mi enemigo')
    
# hijos
class Amorfo(Animal):
  pass

class Mamifero(Animal):
  def __init__(self, name, age, velocity, acuatic, milk):
    super().__init__(name, age, velocity, acuatic)
    self.milk = milk
  
  def getDrink(self):
    print('Drinking milk')

# main
amorfo = Amorfo('caracol', 1, 1, True)
amorfo.defend()

mamifero = Mamifero('Oso', 356, 45, True, 80)
print(mamifero.milk)
mamifero.getDrink()

animal = Animal('Perro', 45, 40, True)
print(animal.name)