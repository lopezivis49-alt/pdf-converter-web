import streamlit as st
from pdf2docx import Converter

st.title("PDF → Word")
pdf = st.file_uploader("PDF", type="pdf")
if pdf and st.button("Convertir"):
    cv = Converter(pdf)
    cv.convert("salida.docx")
    cv.close()
    with open("salida.docx","rb") as f:
        st.download_button("Descargar", f.read(), "word.docx")
