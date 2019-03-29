# Person: Record some info about a few people in a dictionaries. Make a list of 
# them and print everything recorded in the dictionaries for each person.

person_1 = {
    'firstName': 'phil',
    'lastName': 'regan',
    'age': 34,
    'city': 'louisville',
    }
person_2 = {
    'firstName': 'dusty',
    'lastName': 'rhodes',
    'age': 57,
    'city': 'austin',
    }
person_3 = {
    'firstName': 'darleen',
    'lastName': 'summers',
    'age': 22,
    'city': 'plano',
    }

people = [person_1, person_2, person_3]

for person in people:
    print (person['firstName'].title() + " " + person['lastName'].title() +
    " is " + str(person['age']) + " years old, from " + person['city'].title())