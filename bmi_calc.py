feet = int(input("Height (feet only): "))
inches = int(input("Height (inches only): "))
weight = int(input("Weight in pounds: "))

mheight = ((feet+(inches)*1/12)*0.3048)
kweight = (weight*0.453592)
bmi = round((kweight/(mheight**2)),2)
print(f"Your BMI is: {bmi}")