responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb someday? ")

    # Store name and response in responses.
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would anyone else like to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show results.

    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")