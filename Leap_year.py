a = int(input("Enter the year: "))

if a%4 == 0:
    if a%100 ==0:
        if a%400 == 0:
            print("The year is leap year.")
        else:
            print("Not leap year.")
    else:
        print("leap year.")
else:
    print("Not leap year.")