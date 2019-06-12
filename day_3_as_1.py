def printSeriesIncrease(c, n):
    for i in range(n):
        print(c * i)
    return

def printSeriesDecrease(c, n):
    for i in range(n, 0, -1):
        print(c * i)
    return

c = input("Enter a character: ")
n = int(input("Enter a limit: "))
m = int(input("Enter a limit: "))

printSeriesIncrease(c, n)
printSeriesDecrease(c, m)
