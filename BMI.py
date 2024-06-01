weight = float(input("Enter your weight in kilogram(kg): "))
height = float(input("Enter your height in centimeters(cm): "))

# BMI= Body Mass Index

BMI = (weight/height/height) * 10000
print(BMI)

if BMI < 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are at normal weight.")
elif BMI <= 29.9:
    print("You are at overweight.")
    print("Exercise your body. You can go for a run, jump an obstacle or ride a bicycle.")
elif BMI <= 34.9:
    print("You are at severely obese.")
    print("Exercise your body.")
elif BMI > 40:
    print("You are at morbidly obese.")
    print("Exercise your body.")