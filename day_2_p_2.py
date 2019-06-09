#minute in a year

year = int(input("Enter a year: "))

if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print("Leap year")
    print("Number of minutes: ", 366 * 24 * 60)
else:
    print("Non leap year")
    print("Number of minutes: ", 365 * 24 * 60)
