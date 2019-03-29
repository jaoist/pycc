#Keep entering pizza toppings until active is False.

prompt = "\nWhat sort of toppings would you like?"
prompt += "\nEnter 'quit' when you have added all of your toppings! "

active = True

while active == True:
    toppings = input(prompt)
    
    if toppings == 'quit':
        active = False
    else:
        print(toppings.title()+"? Nice! I'll throw it on your pizza.")

