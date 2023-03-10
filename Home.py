import pandas
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit sulce")
    content = """
    Hi, I am Ardit ! Blablabla ...
    """
    st.info(content)

content2 ="""
"This is a new block blablabla !"
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) # this is for

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

