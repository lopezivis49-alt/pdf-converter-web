import streamlit as st
import pdfplumber
from pdf2docx import Converter
import io

st.set_page_config(page_title="PDF to Word", layout="wide")
st.title("🔥 PDF → Word **GRATIS**")

uploaded_file = st.file_uploader("📤 **Sube PDF**", type="pdf")

if uploaded_file is not None:
    # Preview
    with pdfplumber.open(uploaded_file) as pdf:
        if pdf.pages:
            st.image(pdf.pages[0].to_image(resolution=100).original, 
                    caption="**Página 1 Preview**", use_column_width=True)
    
    if st.button("**🚀 CONVERTIR**", type="primary"):
        with st.spinner("Convirtiendo..."):
            cv = Converter(uploaded_file)
            cv.convert("output.docx")
            cv.close()
            
            with open("output.docx", "rb") as f:
                st.download_button(
                    label="📥 **DESCARGAR WORD**",
                    data=f.read(),
                    file_name="pdf_a_word.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
    
    st.balloons()
    st.success("✅ **Funciona en móvil!**")

