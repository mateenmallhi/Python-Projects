import streamlit as st

# Function to perform addition
def addition(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtraction(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiplication(num1, num2):
    return num1 * num2

# Function to perform division
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None

# Dictionary mapping operation names to functions
operations = {
    'Addition': addition,
    'Subtraction': subtraction,
    'Multiplication': multiplication,
    'Division': division
}

st.title('Mateen Mallhi')

# to select operation
operation = st.selectbox(
    'Select Operation',
    ('Addition', 'Subtraction', 'Multiplication', 'Division')
)

# Input numbers
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

result = None

# Perform operation when Calculate button is clicked
if st.button('Calculate'):
    if operation in operations:
        result = operations[operation](num1, num2)
        if result is None and operation == 'Division':
            st.error("Error: Division by zero is not allowed.")

# Display result
if result is not None:
    st.success(f'Result of {operation}: {result}')

