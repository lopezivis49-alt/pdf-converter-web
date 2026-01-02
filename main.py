import streamlit as st
from pdf2docx import Converter

st.title("🔥 PDF → Word **GRATIS**")

# Upload
pdf_file = st.file_uploader("📤 Sube PDF", type="pdf")

if pdf_file is not None:
    st.success("✅ PDF cargado!")
    
    if st.button("**🚀 CONVERTIR A WORD**", type="primary"):
        with st.spinner('Convirtiendo... ⏳'):
            # Convertir
            cv = Converter(pdf_file)
            cv.convert("converted.docx")
            cv.close()
        
        # Descargar
        with open("converted.docx", "rb") as f:
            st.download_button(
                label="📥 **DESCARGAR WORD**",
                data=f.read(),
                file_name="pdf_a_word.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        
        st.balloons()
        st.markdown("---")
        st.markdown("**📱 Móvil**: Añade a pantalla inicio")
