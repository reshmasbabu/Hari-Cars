import streamlit as st
import pandas as pd

# Read the Excel file
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

# Streamlit app
st.title("Find My Car from Hari's Collections")

# Create a search box
search_query = st.text_input("Enter the car name:")

# Filter the DataFrame based on the search query
filtered_df = df[df['Name'].str.contains(search_query, case=False, na=False)]

# Display the filtered results
st.dataframe(filtered_df)
