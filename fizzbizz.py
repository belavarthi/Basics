#Bhargava Elavarthi
for x in range(1,20):
    if x % 3 == 0 and x% 5 == 0:
        print("FizzBuzz")
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

