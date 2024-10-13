# Дополнительное практическое задание по модулю
# Задание "Они все так похожи":

class Figure:
    sides_count = 0
    def __init__(self,__color, *sides):
        self._sides = []
        self.__color = __color
        self.filled = False

        if not self.__is_valid_sides(*sides):
            self._sides = [1] * self.sides_count  # по умолчанию
        else:
            self._sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, lenght):
        super().__init__(color, lenght)
        self.__radius = lenght / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self._sides
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        if s <= 0:
            return 0
        return s

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *([side] * self.sides_count))

    def get_volume(self):
        side = self._sides[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())