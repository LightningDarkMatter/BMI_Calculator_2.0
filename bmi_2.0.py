height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight / (height ** 2),1)

if bmi < 16:
    print(f"You are severely underweight. Your BMI is {bmi}.")
elif 16 <= bmi < 18.5:
    print(f"You are underweight. Your BMI is {bmi}.")
elif 18.5 <= bmi < 25:
    print("You are normal.")
elif 25 <= bmi < 30:
    print(f"You are overweight. Your BMI is {bmi}.")
elif 30 <= bmi < 35:
    print(f"You are obese. Your BMI is {bmi}.")
elif 35 <= bmi < 40:
    print(f"You are severely obese. Your BMI is {bmi}.")
elif bmi >= 40:
    print(f"You are morbidly obese. Your BMI is {bmi}.")
else:
    print("You are a god.")
