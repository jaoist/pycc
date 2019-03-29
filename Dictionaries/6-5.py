# Rivers! Key-value pairs of rivers and the lands they flow through.abs

rivers = {
    'ohio' : 'United States of America',
    'danube' :'Germany and a bunch of other countries in Europe',
    'congo' : 'Angola, Burundi, Cameroon, Central African Republic, '
        'Democratic Republic of the Congo, Gabon, Republic of the Congo, '
        'Rwanda, Tanzania, Zambia',
    }
for name, country in rivers.items():
    print("The " + name.title() + " river runs through " + country + ".")
    print(name)
    print(country)
    print('')
