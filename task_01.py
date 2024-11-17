# Завдання 1: Інкапсуляція
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)
# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). 
# Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.

from abc import ABC, abstractclassmethod

class User(ABC):

    def __init__(self, name, email, password) -> None:
        self._name = name
        self._email = email
        self._password = password

    def get_data(self):
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Password: {self._password}")

    def set_name(self, name):
        self._name = name
        print(f"New name: {self._name}")

    def set_email(self, email):
        self._email = email
        print(f"New email: {self._email}")

    def set_password(self, password):
        self._password = password
        print(f"New password: {self._password}")    

user_01 = User("Mykhailo", "Mykhailo@gmail.com", "qwerty12345")
user_01.get_data()
user_01.set_name("Mike")
user_01.set_email("Mike@gmail.com")
user_01.set_password("ABC123")