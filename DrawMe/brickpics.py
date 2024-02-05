import streamlit as st



st.set_page_config(
    page_title="Convert image to Lego Art",
    layout="wide",
    initial_sidebar_state="expanded"
)

outputName = st.sidebar.text_input("Name of artwork")
inputFile = st.sidebar.file_uploader("Select an image", type=["jpg"])
generateButton = st.sidebar.button("Generate Brick Pick")