import streamlit as st

# Title of the app
st.title("Unit Converter")

# Converter options
conversion_options = ["Length", "Weight", "Temperature"]
selected_conversion = st.selectbox("Select the type of conversion:", conversion_options)

# Conversion Logic
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'feet': 3.28084,
        'miles': 0.000621371,
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274,
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# User input based on selected conversion type
if selected_conversion == "Length":
    st.subheader("Length Converter")
    length_units = ['meters', 'kilometers', 'feet', 'miles']
    input_value = st.number_input("Enter the value:")
    from_unit = st.selectbox("From:", length_units)
    to_unit = st.selectbox("To:", length_units)
    if st.button("Convert"):
        result = length_converter(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result} {to_unit}")

elif selected_conversion == "Weight":
    st.subheader("Weight Converter")
    weight_units = ['kilograms', 'grams', 'pounds', 'ounces']
    input_value = st.number_input("Enter the value:")
    from_unit = st.selectbox("From:", weight_units)
    to_unit = st.selectbox("To:", weight_units)
    if st.button("Convert"):
        result = weight_converter(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result} {to_unit}")

elif selected_conversion == "Temperature":
    st.subheader("Temperature Converter")
    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    input_value = st.number_input("Enter the value:")
    from_unit = st.selectbox("From:", temperature_units)
    to_unit = st.selectbox("To:", temperature_units)
    if st.button("Convert"):
        result = temperature_converter(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result} {to_unit}")
