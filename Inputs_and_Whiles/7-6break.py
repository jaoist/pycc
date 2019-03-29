
prompt = "\nWhat sort of toppings would you like?"
prompt += "\nEnter 'quit' when you have added all of your toppings!"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        
        break
    
    else:
        print(toppings.title()+"? Nice! I'll throw it on your pizza.")