# Program to calculate a person's Body Mass Index (BMI) based on user input in kilograms and centimetres

# Weight equals 65kg
weight = float(input("Enter Weight in Kilograms: "))

# Height equals 180 cm
height = float(input("Enter Heights in Centimeters:  "))

# Convert cm to m2
heightm2 = (height/100)**2

# BMI Calculation
BMI = weight/heightm2

# Output should equal 20.06
print("Your BMI is",BMI)
