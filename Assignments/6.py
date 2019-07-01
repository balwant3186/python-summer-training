a = [10, 15, 20, 25, 30, 35, 40]
b = [25, 40, 35]

def Diff(a, b):
    return list(set(a) - set(b))

print(Diff(a, b))
