import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et doloremagna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis autr irure dolor in reprehenderit in volupate velit esse cillum bolore eu fugiat nulla paiatur. excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

st.write(content)

st.header("Our Team")

col1, emptycol1, col2, emptycol2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])
df = pandas.read_csv('data (2).csv', sep=",")
with col1:
    for index, row in df[:4].iterrows():
        firstandlast = f'{row['first name'].capitalize()} {row['last name'].capitalize()}'
        st.header(firstandlast)
        st.write(row['role'])
        st.image('images2/' + row['image'])
with col2:
    for index, row in df[4:8].iterrows():
        firstandlast = f'{row['first name'].capitalize()} {row['last name'].capitalize()}'
        st.header(firstandlast)
        st.write(row['role'])
        st.image('images2/' + row['image'])
with col3:
    for index, row in df[8:].iterrows():
        firstandlast = f'{row['first name'].capitalize()} {row['last name'].capitalize()}'
        st.header(firstandlast)
        st.write(row['role'])
        st.image('images2/' + row['image'])