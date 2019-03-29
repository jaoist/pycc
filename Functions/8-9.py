"""Pass list of magicians to function to print"""

def make_great(magicians):
    """
    Make add great to list of magicians. We need to deconstruct our list into
    a new holding list, and then redefine the holding list to the original arg.
    """
    
    great_magicians = []

    while magicians:
        magician = magicians.pop() #Removes variable from list and assigns
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    """ 
    At this point the magicians list is empty. Rebuild and return here.
    """
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians
    

def showtime(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ['houdini', 'blaine', 'copperfield']
showtime(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
showtime(great_magicians)

print("\nOriginal magicians:")
showtime(magicians)