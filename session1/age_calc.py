yob = int(input ("your age of birth? "))
age = 2018 - (yob)
print (age)

if age < 1:
    print("new born")
elif age < 18:
    print("teenager")
elif age < 25:
    print("young")
else:
    print("old")