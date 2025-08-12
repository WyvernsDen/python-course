weight = float(input("Type in your weight in kilograms: "))
height = float(input("Type in your height in meters: "))
bmi = round(weight / (height*height), 2)
print(f"Your BMI is {bmi}")