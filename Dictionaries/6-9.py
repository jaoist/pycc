# Favorite places. Create a dictionary of favorite places and tell everyone
# about them.

favorite_places = {
    'tyler' : ['paris', 'ceylon', 'tasmania'],
    'geramy' : ['germany', 'sweden', 'montana'],
    'justin' : ['mexico', 'maine', 'california']
    }

# Adding more than one variable in a for loop will assign items in the dict to
# the variables in sequence.
for name, places in favorite_places.items():
    print(name.title() + " likes these places:")
    for place in places:
        print(" -- " + place.title())