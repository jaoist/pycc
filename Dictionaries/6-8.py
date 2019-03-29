# Pets. Make a list of a bunch of owner / pet pairings.

# Initialize list for pet storage.
pets = []

pet = {
    'name':'sammy',
    'owner':'henry',
    'species':'cat',
    }

pets.append(pet)

pet = {
    'name':'diamond',
    'owner':'fran',
    'species':'dog',
    }

pets.append(pet)

pet = {
    'name':'chester',
    'owner':'charles',
    'species':'cheetah',
    }

pets.append(pet)   

for pet in pets:
    print("Here is some information about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + value.title()) 