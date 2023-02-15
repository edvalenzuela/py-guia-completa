#import inheritance 
#import inheritance as inhe
from inheritance import *

# main
amorfo = Amorfo('caracol', 1, 1, True)
amorfo.defend()

mamifero = Mamifero('Oso', 356, 45, True, 80)
print(mamifero.milk)
mamifero.getDrink()

animal = Animal('Perro', 45, 40, True)
print(animal.name)