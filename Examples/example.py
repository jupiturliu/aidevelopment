import streamlit as st
import pandas as pd

# Title of the app
st.title("Streamlit Example App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is some text.")

# Markdown
st.markdown("### This is a markdown text")

# Input widgets
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=100, step=1)

# Button
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old.")

# Slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

# Checkbox
if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked!")

# Selectbox
option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# Sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.write("This is the sidebar.")

# File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Display an image
st.image("https://via.placeholder.com/150", caption="Sample Image")

# Display a dataframe
data = {'Column 1': [1, 2, 3], 'Column 2': [4, 5, 6]}
df = pd.DataFrame(data)
st.write("Dataframe example:")
st.dataframe(df)