# Remove all instances of specific values from a list.
#  We're getting rid of the cats.

pets = ['dog', 'cat', 'dog', 'goldfish', 'hamster', 'sloth', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)