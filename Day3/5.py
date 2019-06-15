def checkEvenOdd():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print(num, "is even")
        print("If block executed")
    else:
        print(num, "is odd")
        print("Else block executed")

checkEvenOdd()
