import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀"
)

st.title("🚀 My First Streamlit App")

st.write("Hello! This app is deployed using Streamlit.")

name = st.text_input("What's your name?")

if name:
    st.success(f"Hello, {name}! 👋")

st.subheader("Simple Calculator")

number = st.number_input("Enter a number", value=0)

st.write(f"Double: **{number * 2}**")
st.write(f"Square: **{number ** 2}**")
