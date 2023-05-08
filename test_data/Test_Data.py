from utils.generator import Generator


class Test_Data:
    lat, lon = Generator.generate_random_coordinates()
    phone_number = Generator.generate_phone_number()
    address = Generator.generate_address()
    new_address = Generator.generate_address()
