class Shape:

    def __init__(self, line, triangle, rectangle, nullshape) -> None:
        self.line = line
        self.triangle = triangle
        self.rectangle = rectangle
        self.nullshape = nullshape

class Line(Shape):

    def __init__(self, line, triangle, rectangle, nullshape) -> None:
        super().__init__(line, triangle, rectangle, nullshape)

    def move(self):
        for i in range(self.line):
            print("*",end=" ")


class Triangle(Shape):
    
    def __init__(self, line, triangle, rectangle, nullshape) -> None:
        super().__init__(line, triangle, rectangle, nullshape)
        
    def move(self):
        for i in range(self.triangle):
            for j in range(self.triangle):
                if  j == i or j == 0  or i == self.triangle - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
class Rectangle(Shape):

    def __init__(self, line, triangle, rectangle, nullshape) -> None:
        super().__init__(line, triangle, rectangle, nullshape)

    def move(self):
        for i in range(self.rectangle):
            for j in range(self.rectangle):
                if i == 0 or j == 0 or i == self.rectangle - 1 or j == self.rectangle - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

class NullShape(Shape):

    def __init__(self, line, triangle, rectangle, nullshape) -> None:
        super().__init__(line, triangle, rectangle, nullshape)

    def move(self):
        print("Bo'sh shakil")




line1 = Line(4, 5, 4, 10)
line1.move()
print(end=print())

triagle1 = Triangle(4, 5, 4, 10)
triagle1.move()
print()

rectangle1 = Rectangle(4, 5, 4, 10)
rectangle1.move()
print()

nullshape1 = NullShape(4, 5, 4, 10)
nullshape1.move()