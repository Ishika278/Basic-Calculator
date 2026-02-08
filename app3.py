import streamlit as st

st.title("basic calculator app")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

operation = st.selectbox("Select operation: ",["Add", "Sub", "Multiply", "Divide"])

if st.button("calculate"):
    if operation == "Add":
      st.write(num1 + num2)
    elif operation == "Sub":
       st.write(num1 - num2)
    elif operation == "Multiply":
       st.write(num1 * num2)
    elif operation == "Divide":
       if num2 != 0:
        st.write(num1 / num2)
       else:
          st.error("Division by zero is not allowed.")

