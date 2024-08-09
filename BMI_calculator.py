print("Welcome to BMI calculator!!")

height = float(input("Enter your height: "))

weight = int(input("enter your weight: "))

a = height*height

BMI = weight/a
if BMI < 18.5:
    print("Your BMI is ", BMI, "you are underweight.")
elif BMI < 25:
    print("Your BMI is ", BMI, "you have a normal weight")
elif BMI < 30:
    print("Your BMI is ", BMI, "you are slightly ooverweight.")
elif BMI < 40:
    print("Your BMI is ", BMI, "you are obese.")
else:
    print("Your BMI is ", BMI, "you are clinically obese.")