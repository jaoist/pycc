class Dog():
    """A simple attempt to model a dog. Woof."""

    def __init__(self, name, age): #self is required in the method definition.
        """Initialize name and age attributes."""
        self.name = name
        self. age = age

    def sit(self):
        """Simulate a dog sitting in response to a command. Good boye."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(self.name.title() + " rolled over! Such a good boy!")
    
   
my_dog = Dog('newton', 10)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()