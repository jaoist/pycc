#Keep entering pizza toppings until 'quit' is entered.

prompt = "\nWhat sort of toppings would you like?"
prompt += "\nEnter 'quit' when you have added all of your toppings!"
toppings = input(prompt)

while toppings != 'quit':
    print(toppings.title()+"? Nice! I'll throw it on your pizza.")
    toppings = input(prompt)
    
