import random

"""Класс для генерации тестовых данных"""


class Generator:
    """Метод для генерации широты и долготы"""

    @staticmethod
    def generate_random_coordinates():
        lat = round(random.uniform(-90, 90), 6)
        lng = round(random.uniform(-180, 180), 6)
        return lat, lng

    """Метод для генерации номера телефона"""

    @staticmethod
    def generate_phone_number():
        country_code = "+91"  # код страны

        group1 = str(random.randint(100, 999))
        group2 = str(random.randint(100, 999))
        group3 = str(random.randint(1000, 9999))

        phone_number = "{} {} {} {}".format(country_code, group1, group2, group3)  # объединяем группы цифр в одну строку
        return phone_number

    """Метод для генерации нового адреса"""
    @staticmethod
    def generate_address():
        number = random.randint(1, 100)
        side = random.choice(['north', 'south', 'east', 'west'])
        layout = random.choice(['avenue', 'boulevard', 'street', 'lane'])
        city = random.choice(['cohen', 'smith', 'johnson', 'brown'])
        code = random.randint(1, 20)

        return f"{number}, {side} {layout}, {city} {code:02}"
