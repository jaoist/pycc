prompt = "\nHowdy cowpoke. How old are you? "

give_me_a_ticket = ''
while give_me_a_ticket != 'N':
    age = int(input(prompt))
    if age < 3:
        price = 'Free!'
    elif age > 3 and age < 12:
        price = '$10.'
    else:
        price = '$15.'

    print ("Your ticket is " + price)
    give_me_a_ticket = input("Would you like another ticket? (Y/N):")
    give_me_a_ticket = give_me_a_ticket.upper()