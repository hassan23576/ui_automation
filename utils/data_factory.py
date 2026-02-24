from faker import Faker


class DataFactory:

    def __init__(self):
        self.faker = Faker()


    def first_name(self):
        return self.faker.first_name()

    def last_name(self):
        return self.faker.last_name()

    def email(self):
        return self.faker.email()

    def address(self):
        return self.faker.address().replace("\n", " ")

    def get_full_name(self):
        full_name = f'{self.first_name()} {self.last_name()}'
        return full_name

    def phone_number(self):
        return self.faker.phone_number()

    def mobile_number(self):
        return self.faker.numerify('##########')

    def get_text_box_data(self):
        """Generates the specific dictionary needed for the TextBox page"""
        return {
            'full_name': self.get_full_name(),
            'email': self.email(),
            'address': self.address(),
            'permanent_address': self.address(),
        }
