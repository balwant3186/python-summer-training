def twoCharUpward(c, n):
    for i in range(0, n, 2):
        print(((n-i)//2)*" ", c * i, ((n-i)//2)*" ")
    return

def twoCharDownward(c, n):
    for i in range(n, 0, -2):
        print(((n-i)//2)*" ", c * i, ((n-i)//2)*" ")
    return

c = input("Enter a character: ")
n = int(input("Enter a limit: "))
m = int(input("Enter a limit: "))

twoCharUpward(c, n)
twoCharDownward(c, m)
