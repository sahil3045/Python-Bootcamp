a = int(input("Enter the year to check weather it is leap year or not: "))

if a%4 == 0:
    if a%100 ==0:
        if a%400 == 0:
            print("Year is leap year.")
        else:
            print("Year is not a leap year.")
    else:
        print("Year is leap year.")
else:
    print("Year is not a leap year.")