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

    def calculate_area(self, radius):
        square = 3.14 * radius * radius
        print(f"Square of Circle with radius {radius} is {square}")

circle_01 = Circle(3)
circle_01.calculate_area()