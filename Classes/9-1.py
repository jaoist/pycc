class Restaurant():
    """Model of a restaurant that has two methods."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name.capitalize() + " serves " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.name.capitalize() + " is now open.")

my_restaurant = Restaurant("vinnie's" , "pizza")

print(my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()