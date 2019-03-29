mynum = input("Give me a number: ")
num_mod  = int(mynum) % 10

if (num_mod == 0):
    print(mynum + " " + "is a multiple of ten.")
else:
    print(mynum + " " + "is not a multiple of ten")