# Ask the user to input weight in kilograms and height in meters
height = float(input("Your height in meters:"))
weight = float(input("Your weight in kilograms:"))

#Calculate the BMI
BMI = weight / (height * height)

#Print BMI
print("Your BMI is:", BMI)

#Define the categorys
underweight = BMI < 18.5
normal = 18.5 <= BMI < 24
overweight = 25 <= BMI < 29.9 

#Determine the BMI category
if underweight:
    print("Underweight")
elif normal:
    print("Normal")
elif overweight:
    print("Overweight")
else:
    print("Obeise")

#Raccomandation based on category
if underweight:
    print("You may want to gain some weight.")
elif normal:
    print("You are in a healthy weight range.")
elif overweight:
    print("You may want to consider losing some weight.")
else:
    print("You should consult a doctor for health advice.")




