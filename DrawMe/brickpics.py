import streamlit as st
from PIL import Image
from io import BytesIO
from drawbrickpic import LegoArtPic
from drawbrickpic import generatePillArt

defaultLegoArtPic = LegoArtPic(50, 48, 48)

st.set_page_config(
    page_title="Convert image to Lego Art",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("BRICK PICS")
st.markdown("For best results upload an image with 1:1 aspect ratio, or as close as possible")

tabOriginal, tabBrickPick, tabLegend, tabSplit = st.tabs(["Original", "Brick Pick", "Legend", "Split"])

outputName = st.sidebar.text_input("Name of artwork", value="BrickPick1")
inputFile = st.sidebar.file_uploader("Select an image", type=["jpg"], accept_multiple_files=False)
generateButton = st.sidebar.button("Generate Brick Pick")

if inputFile is not None:
    uploadedFile = Image.open(inputFile)
    tabOriginal.image(uploadedFile)
    outputImage = generatePillArt(defaultLegoArtPic, uploadedFile, "NothingYet.jpg")
    tabBrickPick.image(outputImage, outputName)