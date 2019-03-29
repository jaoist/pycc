favNums = {
    'ken':[12,24,66],
    'jackson':[34,890,7],
    'tim':[44444,8609834,90923409],
    'harrison':[1,2,3,4],
    'peanut':[42,0.07],
    }
for name, numbers in favNums.items():
    print(name.title() +  " likes these numbers:")
    for number in numbers:
        print(" # " + str(number))