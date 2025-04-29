class Person:
    message_counter = 0
    # объявите ваш метод
    def print_number_of_messages(self):
        print(self.message_counter)

id_1 = Person()
id_2 = Person()

id_1.message_counter = 5
id_2.message_counter = 10

# ваш код вызова метода:
id_1.print_number_of_messages()
id_2.print_number_of_messages()
