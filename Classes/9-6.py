from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """A facsimilie of an icecream stand. Subclass of the Restaurant class"""

    def __init__(self, name, cuisine_type, number_served=0):
        super().__init__(name, cuisine_type, number_served)
        self.flavors = ['vanillia', 'chocolate', 'banana', 'strawberry']

    def list_flavors(self):
        """Print off our list of flavors."""
        
        flavor_count = 0
        for flavor in self.flavors:
            flavor_count += 1
        
        message = "We have "
        for flavor in self.flavors:
            flavor_count -= 1
            if flavor_count > 0:
                message += flavor.title() + ", "
            elif flavor_count == 0:
                message += "and " + flavor.title() + "."
        
        print(message)

my_icecreamstand = IceCreamStand("Frozen Treats", "Ice Cream")
my_icecreamstand.list_flavors()