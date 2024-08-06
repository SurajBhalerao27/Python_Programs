class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def cal_area(self):
        pass
    
class Rectangle(Shape):
    def cal_area(self):
        return self.width * self.height
    
rect = Rectangle(40,5)
print(f'Rectangle area : {rect.cal_area()}')