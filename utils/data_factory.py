from faker import Faker


class DataFactory:

    def __init__(self):
        self.faker = Faker()


    def get_first_name(self):
        return self.faker.first_name()

    def get_last_name(self):
        return self.faker.last_name()

    def get_email(self):
        return self.faker.email()

    def get_address(self):
        return self.faker.address()

    def get_full_name(self):
        full_name = f'{self.get_first_name()} {self.get_last_name()}'
        return full_name

    def get_text_box_data(self):
        """Generates the specific dictionary needed for the TextBox page"""
        return {
            'full_name': self.get_full_name(),
            'email': self.get_email(),
            'address': self.get_address().replace("\n", " "),
            'permanent_address': self.get_address().replace("\n", " "),
        }
