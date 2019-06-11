def twoCharUpward(char, n):
    for i in range(0, n, 2):
        print(((n-i)//2)*" ", char * i, ((n-i)//2)*" ")
    return

def twoCharDownward(char, n):
    for i in range(n, 0, -2):
        print(((n-i)//2)*" ", char * i, ((n-i)//2)*" ")
    return

char = input("Enter a character: ")
n = int(input("Enter a incremental series limit: "))
m = int(input("Enter a decremental series limit: "))

twoCharUpward(char, n)
twoCharDownward(char, m)
