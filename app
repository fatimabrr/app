import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# Streamlit app title
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", step=1e-6, format="%.6f")
num2 = st.number_input("Enter second number", step=1e-6, format="%.6f")

# Dropdown for selecting operation
operation = st.selectbox("Choose operation", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

# Button to perform calculation
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")

