# Cities dictionary. A dict inside of a dict.abs

cities = {
    'amsterdam':{
        'country': 'netherlands',
        'population': 851573,
        'fact': 'This city is below sea level.',
        },
    'hiroshima':{
        'country': 'japan',
        'population': 1196274,
        'fact': 'One of two cities to have ever been the target of an atom' 
        ' bomb.',
        },
    'new york city':{
        'country': 'united states of america',
        'population':8537673,
        'fact': 'World''s 12th largest economy by GDP'
        },
    }

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact']

    print(city.title() + " is in " + country)
    print("\t" + "It has a population of " + str(population))
    print("\t" + fact + "\n")
