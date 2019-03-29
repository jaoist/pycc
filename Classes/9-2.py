class Restaurant():
    """Model of a restaurant that has two methods."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " serves " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.name.title() + " is now open.")

my_restaurant = Restaurant("vinnie's" , "pizza")
print(my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

rest_1 = Restaurant("Green Room", "Vegan")
print(rest_1.name)
print(rest_1.cuisine_type)
rest_1.describe_restaurant()
rest_1.open_restaurant()

rest_2 = Restaurant("the buttered bovine", "Steakhouse")
print(rest_2.name)
print(rest_2.cuisine_type)
rest_2.describe_restaurant()
rest_2.open_restaurant()