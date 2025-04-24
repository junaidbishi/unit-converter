
import streamlit as st

st.title("Unit Converter 🌍")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Select category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Select conversion unit based on category
if category == "Length":
    unit = st.selectbox("Select a conversion", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select a conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select a conversion", [
        "Seconds to minutes", "Minutes to seconds",
        "Hours to minutes", "Minutes to hours",
        "Hours to days", "Days to hours"
    ])

# Input value to convert
value = st.number_input("Enter a value to convert", value=0.0)

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
