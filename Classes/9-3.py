class User():
    """Create a profile for a user."""
    
    def __init__(self, first_name, last_name, age, gender, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)
        print("Location: " + self.location)
        print("Occupation: " + self.occupation)

    def greet_user(self):
        print("Login successful. Hello, " + self.first_name + " " + 
                self.last_name)

user_1 = User('dan', 'harrison', 24, 'gay male', 'texas', 'cowboy')
user_1.describe_user()
user_1.greet_user()

user_2 = User('greta', 'tremma', 32, 'straigt female', 'united kingdom', 'air hostess')
user_2.describe_user()
user_2.greet_user()

user_3 = User('benji', 'brody', 54, 'rocket ship', 'alabama', 'gas station worker')
user_3.describe_user()
user_3.greet_user()