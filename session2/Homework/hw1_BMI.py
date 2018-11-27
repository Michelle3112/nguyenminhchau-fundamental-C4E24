a = float(input("What is your height (cm)?"))
b = float(input("What is yout weight (kg)?"))
c = a*0.01
BMI = b / (c * c)
print(BMI)

if BMI < 16:
    print("Severely")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal")
elif BMI < 30:
    print("overweight")
else:
    print("obese")

