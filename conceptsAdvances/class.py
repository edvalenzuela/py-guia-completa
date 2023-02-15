
class Gato():
  life= 100
  damage= 150
  
  def __init__(self, name, age, velocity):
    self.name = name
    self.age = age
    self.velocity = velocity
  
  def takingDamage(self, dmgRecieve):
    self.life -= dmgRecieve
  
gato = Gato('Tom', 7, 100)
print(gato.name, str(gato.age), str(gato.velocity))

gato.takingDamage(10)
print('vida actual', gato.life)

# modificando una propiedad directamente
gato.age = 11
gato.life= 20
print(gato.name, str(gato.age), str(gato.velocity))
    
    