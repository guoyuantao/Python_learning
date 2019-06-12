class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name)
        print("The restaurant's type is " + self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is open!')

