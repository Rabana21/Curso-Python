import random
import copy
# Consider using the modules imported above.

def dict_to_list(dic):
  lst = list()
  for (colour,amount) in dic.items():
    for i in range(amount):
      lst.append(colour)
  return lst

class Hat: 
  def __init__(self,**kwargs):
    self.contents = dict_to_list(kwargs)

  def draw(self, number):
    draw = list()
    if number >= len(self.contents):
      draw = self.contents
      self.contents = list()
      return draw
    while len(draw) < number:
      index = random.randint(0, len(self.contents)-1)
      draw.append(self.contents.pop(index))
    return draw

  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  hit = 0
  
  for _ in range(num_experiments):
    expected = dict_to_list(expected_balls)
    copy_hat = copy.deepcopy(hat)
    #print('Contenido del sombrero',copy_hat.contents)
    resault = copy_hat.draw(num_balls_drawn)
    #print(resault)
    found = True
    while len(expected) > 0 and found:
      if expected[0] in resault :
        elem = expected[0]
        expected.pop(0)
        resault.pop(resault.index(elem))
      else: 
        found = False
    if found:
      hit += 1
  return hit / num_experiments