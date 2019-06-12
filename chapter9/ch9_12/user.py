class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print('name: ' + self.first_name + ' ' + self.last_name, '年龄：' + str(self.age))

    def greet_user(self):
        print('Happy a good day!' + self.first_name + ' ' + self.last_name)
