def checkEven():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is even")
    return None

def checkOdd():
    num = int(input("Enter a number: "))
    if num % 2 == 1:
        print(num, "is odd")
    return None

checkEven()
checkOdd()
