class Rectangel():
       def __init__(self, length, width):
        self.length = length
        self.width = width

class Square():
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width 

class Cube(Rectangel):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length*self.width*self.height


quare = Square(3, 4)
cube = Cube(2, 3, 4)

print(quare.area())