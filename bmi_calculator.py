weight = float(input('Enter weight in Kg: '))
height = float(input('Enter height in cm: '))
h = height * 0.01
bmi = weight / h**2

if bmi < 18.5:
    print("Indicates person is underweight")
    print("Dietary Recommendations: “You’re lighter than average! 💡 Add more healthy calories – nuts, milk, eggs, and whole grains can help you gain strength.”")
elif bmi >= 18.5 and bmi < 25.0:
    print("Indicates person has healthy weight relative to a person's height")
    print("“Great job! 🎉 You’re in the healthy range. Keep enjoying balanced meals, stay active, and maintain your lifestyle.”")
elif bmi >= 25.0 and bmi < 30.0:
    print("Indicates person is overweight")
    print("“You’re doing well, but a little lighter will be even better 🌟. Try more veggies, fruits, and daily walks.”")
elif bmi >= 30.0 and bmi < 35.0:
    print("Indicates person is obese")
    print("“Your health matters ❤️. Small steps like skipping sugary drinks and adding short walks can make a big difference. Consider expert advice too.”")
elif bmi >= 35.0:
    print("Indicates person is extreme obese")
    print("“You’re strong 💪, but your body needs extra care now. 🌟 Focus on gentle daily activity, lighter meals, and definitely seek guidance from a health professional. Small changes = Big results!”")