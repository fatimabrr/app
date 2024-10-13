import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", format="%f")
num2 = st.number_input("Enter the second number", format="%f")

# Dropdown to select operation
operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculate result based on the selected operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("The result is:", result)

