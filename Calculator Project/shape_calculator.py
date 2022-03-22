class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    str = ''
    if self.width > 50 or self.height > 50:
      str = 'Too big for picture.'
    else:
      for i in range(self.height):
        for j in range(self.width):
          str += '*'
        str += '\n'
    return str

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()

  def __str__(self): 
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'


class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height

  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'
