class Cat(object):
  def __init__(self, name):
    self.name = name
    self.nearby_cats = {}
    
A = Cat('A')
B = Cat('B')
C = Cat('C')
D = Cat('D')

A.nearby_cats[B] = 2
A.nearby_cats[C] = 4
B.nearby_cats[D] = 5

def find_fluff(original_cat, distance):
  result = []
  
  for cat in original_cat.nearby_cats:
    if (original_cat.nearby_cats[cat] <= distance):
      nearby_cats.append(cat.name)
    
      nearby_cats = nearby_cats + find_fluff(cat, distance - original_cat.nearby_cats[cat])
  
  return result