import random

class Human:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth

class Visitor(Human):
    def __init__(self, name, sex, year_of_birth, hair_length, nail_length, nail_color=""):
        super().__init__(name, sex, year_of_birth)
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color if nail_color else "бесцветные"

class Manicurist(Human):
    def do_job(self, Visitor):
        if Visitor.nail_length > 1:
           Visitor.nail_length -= 1
           Visitor.nail_color = random.choice(["красный", "фиолетовый", "зелёный"])

class Hairdresser(Human):
     def do_job(self, Visitor):
        if Visitor.hair_length > 1:
           Visitor.hair_length -= 1

class Barber(Human):
    def do_job(self, Visitor):
        if Visitor.sex == "M":
            if Visitor.hair_length > 1:
               Visitor.hair_length -= 1
        else:
            raise ValueError(f"Барбер {self.name} стрижет только мужчин")

# Пример использования классов:
neo = Visitor(name="Neo", sex="M", year_of_birth=1964, hair_length=10, nail_length=2)
trinity = Visitor(name="Trinity", sex="F", year_of_birth=1967, hair_length=30, nail_length=5)

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)

manicurist.do_job(neo)
print(f"{neo.name}: Длина ногтей - {neo.nail_length}, Цвет ногтей - {neo.nail_color}")

barber.do_job(neo)
print(f"{neo.name}: Длина волос - {neo.hair_length}")

try:
    barber.do_job(trinity)
except ValueError as e:
    print(f"Ошибка: {e}")
