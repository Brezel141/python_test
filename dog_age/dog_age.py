#Ask user to inser age
age = int(input("Age:"))

#Variabels
age_before_2 = age * 10.5
age_after_2 = 21 + (age - 2) * 4

if age < 0:
    print("Not allowed")
elif age <= 2:
    print("Age dog is:", age_before_2)
else: 
    age > 2
    print("Age dog is:", age_after_2)

