import streamlit as st

def convert_temperature(temp, conversion_type):
    if conversion_type == "Fahrenheit to Celsius":
        return (temp - 32) * 5.0/9.0
    elif conversion_type == "Celsius to Fahrenheit":
        return (temp * 9.0/5.0) + 32

# Streamlit app
st.title("Temperature Converter")

# Get user input
temp_input = st.number_input("Enter the temperature:")
conversion_type = st.selectbox(
    "Select conversion type:",
    ("Fahrenheit to Celsius", "Celsius to Fahrenheit")
)

# Perform conversion when the button is clicked
if st.button("Convert"):
    converted_temp = convert_temperature(temp_input, conversion_type)
    st.write(f"The converted temperature is: {converted_temp:.2f}°")
