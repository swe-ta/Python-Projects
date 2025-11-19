def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def factTrailingZeros(number):
    pass

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    fact = factorial(number)
    print(f"The factorial is:  {fact}")