import streamlit as st

st.title("💪 BMI Calculator")

# Input from user
weight = st.number_input('Enter weight in Kg:', min_value=1.0)
height = st.number_input('Enter height in cm:', min_value=50.0)

if st.button("Calculate"):
    h = height * 0.01
    bmi = weight / (h**2)

    st.write(f"Your BMI is: **{bmi:.2f}**")

    if bmi < 18.5:
        st.write("Indicates person is underweight")
        st.write("💡 You’re lighter than average! Add more healthy calories – nuts, milk, eggs, and whole grains can help you gain strength.")
    elif bmi >= 18.5 and bmi < 25.0:
        st.write("Indicates person has healthy weight relative to a person's height")
        st.write("🎉 Great job! You’re in the healthy range. Keep enjoying balanced meals, stay active, and maintain your lifestyle.")
    elif bmi >= 25.0 and bmi < 30.0:
        st.write("Indicates person is overweight")
        st.write("🌟 You’re doing well, but a little lighter will be even better. Try more veggies, fruits, and daily walks.")
    elif bmi >= 30.0 and bmi < 35.0:
        st.write("Indicates person is obese")
        st.write("❤️ Your health matters. Small steps like skipping sugary drinks and adding short walks can make a big difference. Consider expert advice too.")
    elif bmi >= 35.0:
        st.write("Indicates person is extreme obese")
        st.write("💪 You’re strong, but your body needs extra care now. 🌟 Focus on gentle daily activity, lighter meals, and definitely seek guidance from a health professional. Small changes = Big results!")
