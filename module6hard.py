from math import pi

class Figure:
    sides_count = 0
    def __init__(self, sides, color, filled = False):
        self.sides = sides
        self.color = color
        self.filled = filled
        self.sides_count = len(self.sides)

    def get_color(self):
        return self.color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.color = [r, g, b]
        else:
            pass

    def get_sides(self):
        return self.sides

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == len(self.sides) and all(isinstance(side, int) and side > 0 for side in new_sides):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.sides = list(new_sides)
        else:
            print('Указано неверное количество сторон или не все указанные значения являются целыми положительными числами')

    def __len__(self):
        return sum(self.sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled = False):
        if isinstance(sides, int) == False:
            self.sides = [1] * self.sides_count
            print('Для фигуры "круг" параметр "sides" должен быть целым числом; создан круг с длиной окружности равной 1')
        else:
            self.sides = [sides] * Circle.sides_count
        super().__init__(color, filled)
        self.sides_count = Circle.sides_count

    def get_color(self):
        super().get_color()
        return self.color

    def __len__(self):
        super().__len__()
        return self.__len__()

    @property
    def radius(self):
        return self.sides[0] / (2 * pi)

    def get_square(self):
        return pi * self.radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled = False):
        if isinstance(sides, list) == False or len(sides) != Triangle.sides_count or any(isinstance(side, int) for side in sides) == False:
            self.sides = [1] * self.sides_count
            print('Для фигуры "треугольник" параметр "sides" должен быть списком из 3 элементов, являющихся целыми числами; создан равносторонний треугольник с длиной стороны равной 1')
        else:
            self.sides = sides
        super().__init__(color, filled)
        self.sides_count = Triangle.sides_count

    def get_square(self):
        sp = super().__len__() / 2
        return (sp * (sp - self.get_sides()[0]) * (sp - self.get_sides()[1]) * (sp - self.get_sides()[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled = False):
        if isinstance(sides, int) == False:
            self.sides = [1] * self.sides_count
            print('Для фигуры "куб" параметр "sides" должен быть целым числом; создан куб с ребром равным 1')
        else:
            self.sides = [sides]* self.sides_count
        super().__init__(color, filled)
        self.sides_count = Cube.sides_count

    def get_volume(self):
        return self.sides[0] ** 3




#figure = Figure([4, 6, 8, 3, 5], [37, 156, 210], filled = True)
circle = Circle(7, [89, 148, 96])
#triangle = Triangle([3, 4, 5], [125, 78, 215])
#cube = Cube(7, [89, 194, 235])
#print(figure.get_color())
#figure.set_color(85, 78, 100)
#print(figure.get_color())
# figure.set_sides(8, 1, 7, 9)
#print(figure.get_sides())
# print(figure.__len__())
#print(circle.radius)
#print(triangle.get_square())
#print(cube.get_volume())
#print(figure.sides_count)
#print(cube._Cube__sides)
# print(circle._Circle__sides)
#print(circle.get_square())
# print(circle.__len__())
#print(circle.set_sides(8))
#triangle.set_sides(6, 5, 2)
# print(triangle.get_color())
# print(triangle.get_sides())
#circle.set_color(97, 138, 206)
print(circle.get_color())
print(circle.get_sides())
# print(cube.get_color())
# print(cube.get_sides())
#print(dir(figure))
print(dir(circle))




