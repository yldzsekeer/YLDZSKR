print("Welcome to our programme!")
age = float(input("Please enter your age:"))
if  0 < age <= 19:
    if 0 < age < 1:
        print("You are an infants.")
    if 10 < age <= 19:
        print("You are an adolescent.")
    else:
        print("You are a child.")
elif age > 19:
    print("You are an adult.")
else:
    print("Please enter a valid age.") 