# We're making a pretend deli.

# Make a list that will be populated by sandwich orders.
sandwich_orders = ['ham on rye', 'turkey club', 'cubano', 'monte cristo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)


print("Order up! The " + str(finished_sandwiches) + "are ready!")