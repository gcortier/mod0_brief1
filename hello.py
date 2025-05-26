import streamlit as st

import pandas as pd






st.title("Streamlit : Initiation")
st.write("Hello, Streamlit! 42")


df = pd.read_csv("sales_data_sample.csv")
st.dataframe(df.head())
# st.write(data)



# st.button("Click me!")
# st.text_input("Type something here:")
# st.text_area("Type a longer text here:")
# st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
# st.checkbox("Check me!")
# st.radio("Select one:", ["Choice A", "Choice B", "Choice C"])
# st.slider("Select a value:", 0, 100, 50)
# st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
# st.date_input("Select a date:")
