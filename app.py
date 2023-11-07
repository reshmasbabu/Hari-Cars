import pandas as pd
import streamlit as st

# Read the Excel file
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)


def add_bg_from_url():

    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1515281239448-2abe329fe5e5?q=80&w=1793&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()


# Define the background color, text color, text content, and text style
background_color = "white"
text_color = "red"
text_content = "Find My Car from Hari's Collections"
text_style = "font-size: 24px; font-weight: bold; text-align: center;"
text_box_height = "50px"  # Adjust the height as needed

# Define the CSS styles for the smaller white textbox with red letters and text style
css_style = f"background-color: {background_color}; color: {text_color}; padding: 10px; height: {text_box_height};"

# Use st.markdown to display the styled text
st.markdown(f'<div style="{css_style}"><p style="{text_style}">{text_content}</p></div>', unsafe_allow_html=True)


# Create a search box
search_query = st.text_input("Enter the car name:")

# Filter the DataFrame based on the search query
filtered_df = df[df['Name'].str.contains(search_query, case=False, na=False)]

# Display the filtered results with custom width and height
st.dataframe(filtered_df, width=400, height=0)
