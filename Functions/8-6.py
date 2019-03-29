def city_country(city_name , country):
    print(city_name.title() +", "+ country.title())

city_list = {'tokyo':'japan', 'beijing':'china', 'seoul':'korea'}

for city, country in city_list.items():
    city_country(city, country)