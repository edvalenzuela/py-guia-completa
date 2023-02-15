from enum import Enum

class FoodWithoutEnum:
  SANDWITCH= 1
  SALAD= 2
  MEAT= 3
  FISH= 4
  
# enum
class Food(Enum):
  SANDWITCH= 1
  SALAD= 2
  MEAT= 3
  FISH= 4

print(FoodWithoutEnum.FISH)
print(Food.FISH)

if Food.FISH is Food.FISH:
  print('Aquí tiene su pescado sr')