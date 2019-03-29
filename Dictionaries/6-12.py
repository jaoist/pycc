# Cities dictionary. A dict inside of a dict. Extended formatting.

cities = {
    'amsterdam':{
        'country': 'netherlands',
        'population': 851573,
        'fact': 'is below sea level.',
        },
    'hiroshima':{
        'country': 'japan',
        'population': 1196274,
        'fact': 'is one of two cities to have ever been the target of an atom' 
        ' bomb.',
        },
    'new york city':{
        'country': 'united states of america',
        'population':8537673,
        'fact': 'is the world''s 12th largest economy by GDP'
        },
    }

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact']

    print(city.title() + " is in " + country)
    print("\t" + "It has a population of " + str(population))
    print("\t" + city.title() + " " + fact + "\n")
