for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBazz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Bazz")
    else:
        print(x)
