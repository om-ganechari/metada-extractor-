import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
from docx import Document

st.set_page_config(page_title="MetaSniff", page_icon="🔍")

st.title("🔍 MetaSniff - Metadata Extractor")
st.markdown("Upload **Image**, **PDF**, or **Word** file to view metadata.")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf", "docx"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()

    if file_type in ['jpg', 'jpeg', 'png']:
        st.subheader("🖼️ Image EXIF Metadata")
        try:
            image = Image.open(uploaded_file)
            exif_data = image._getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    st.write(f"**{tag_id}** : {value}")
            else:
                st.info("No EXIF metadata found.")
        except Exception as e:
            st.error(f"Error: {e}")

    elif file_type == 'pdf':
        st.subheader("📄 PDF Metadata")
        try:
            reader = PdfReader(uploaded_file)
            metadata = reader.metadata
            if metadata:
                st.json(metadata)
            else:
                st.info("No metadata found.")
        except Exception as e:
            st.error(f"Error: {e}")

    elif file_type == 'docx':
        st.subheader("📝 Word Document Metadata")
        try:
            doc = Document(uploaded_file)
            props = doc.core_properties
            st.write({
                "Title": props.title,
                "Author": props.author,
                "Created": str(props.created),
                "Last Modified": str(props.modified),
                "Last Printed": str(props.last_printed),
            })
        except Exception as e:
            st.error(f"Error: {e}")
