# Sandwiches. Accept a list of items that we want on a sandwich.

def make_sandwich(*items):
    print("\nAdding your choices to make a tasty sandwich:")
    for item in items:
        print("- " + item)

make_sandwich('mustard','pickles','turkey','salami')
make_sandwich('mustard','cheese','turkey','salami')