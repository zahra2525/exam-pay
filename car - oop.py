class car: 
  def __init__(self, carname, color , year , speed):
    self.carname = carname
    self.color = color
    self.year = year
    self.speed = speed
  def car(self):
    print(self.carname, self.color, self.year, self.speed)
car1 = car('pershiya', 'sefid', 2001 ,200)
car1.car()