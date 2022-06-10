class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self): 
    return self.width * self.height
  
  def get_perimeter(self): 
    return (2 * self.width) + (2 * self.height)
  
  def get_diagonal(self): 
    return (self.width ** 2 + self.height ** 2) ** 0.5
  
  def get_picture(self):
    result = ""
    if self.width > 50 or self.height > 50:
      result = "Too big for picture."
    else:
      for i in range(0, self.height):
        for j in range(0, self.width):
          result += "*"
          
        result += "\n"
    return result
  
  def get_amount_inside(self, shape): 
    max_width = self.width // shape.width
    max_height = self.height // shape.height
    
    return max_width * max_height


class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    super().set_width(side)
    super().set_height(side)

  def set_width(self, width):
    self.set_side(width)
  
  def set_height(self, height):
    self.set_side(height)