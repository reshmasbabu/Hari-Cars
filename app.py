import streamlit as st
import pandas as pd

# Read the Excel file
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://unsplash.com/photos/die-cast-car-collection-on-rack-JBrfoV-BZts");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()


st.markdown("<h1 style='color: red;'>Find My Car from Hari's Collections</h1>", unsafe_allow_html=True)

# Create a search box
search_query = st.text_input("Enter the car name:")

# Filter the DataFrame based on the search query
filtered_df = df[df['Name'].str.contains(search_query, case=False, na=False)]

import streamlit as st

# Display the filtered results with custom width and height
st.dataframe(filtered_df, width=400, height=0)
