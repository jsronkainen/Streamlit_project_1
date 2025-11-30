import streamlit as st

# Set page config
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
    layout="centered"
)

# Add a title
st.title("Welcome to My Streamlit App!")

# Add some text
st.write("This is a simple Streamlit application.")

# Add a slider
number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected: {number}")

# Add a button
if st.button("Click me!"):
    st.balloons()
    st.success("Button clicked! 🎉")

# Add a sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("Enter your name:")
if name:
    st.sidebar.write(f"Hello, {name}!")
