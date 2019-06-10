def checkEven(num):
    if num % 2 == 0:
        print(num, "is even")
    return None

def checkOdd(num):
    if num % 2 == 1:
        print(num, "is odd")
    return None

num = int(input("Enter a number: "))
checkEven(num)
checkOdd(num)
