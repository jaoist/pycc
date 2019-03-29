class Restaurant():
    """Model of a restaurant that has two methods."""

    def __init__(self, name, cuisine_type, number_served = 0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.name.capitalize() + " serves " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.name.capitalize() + " is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

restaurant = Restaurant("vinnie's" , "pizza")

print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(35)
print(str(restaurant.number_served))