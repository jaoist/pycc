def car_info(make, model, **other):
    # Build the dictionary 
    info = {}
    info['make'] = make
    info['model'] = model
    for key, value in other.items():
        info[key] = value
    return info

car = car_info('ford', 'focus', color = 'red', seats = 'leather')

print(car)