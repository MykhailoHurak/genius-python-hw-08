# Завдання 2: Абстракція
# Створіть клас "Фігура" (Shape), який буде абстрактним класом. 
# У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
# Створіть підкласи цього класу для різних геометричних фігур, 
# наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). 
# У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

from abc import ABC, abstractclassmethod

class Shape(ABC):

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        square = 3.14 * self.radius * self.radius
        print(f"Square of Circle with radius {self.radius} is {square}")

class Rectangle(Shape):

    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        square = self.side_a * self.side_b
        print(f"Square of Rectangle with side_a={self.side_a}, side_b={self.side_b} is {square}")

class Triangle(Shape):

    def __init__(self, side_a, h) -> None:
        self.side_a = side_a
        self.h = h

    def calculate_area(self):
        square = 1/2 * self.side_a * self.h
        print(f"Square of Triangle with side_a={self.side_a}, high={self.h} is {square}")

circle_01 = Circle(3)
circle_01.calculate_area()

rectangle_01 = Rectangle(5, 6)
rectangle_01.calculate_area()

triangle_01 = Triangle(10, 6)
triangle_01.calculate_area()