# app.py

import streamlit as st
from PIL import Image, ImageOps
from io import BytesIO

st.set_page_config(
    page_title="Document Scanner",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Simple Adobe Scan Style App")
st.write("Upload a document image, convert it to black & white, and download it as a PDF.")

uploaded_file = st.file_uploader(
    "Upload a document image",
    type=["jpg", "jpeg", "png"]
)

def process_image(image):
    """
    Convert image to grayscale and enhance contrast
    for document scanning effect.
    """

    # Convert to grayscale
    gray = ImageOps.grayscale(image)

    # Increase contrast for better scan effect
    bw = gray.point(lambda x: 0 if x < 150 else 255, '1')

    # Convert back to RGB for PDF saving
    final_image = bw.convert("RGB")

    return final_image

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    if st.button("Convert to PDF"):

        # Process image
        processed_image = process_image(image)

        st.subheader("Scanned Black & White Image")
        st.image(processed_image, use_container_width=True)

        # Save PDF to memory
        pdf_buffer = BytesIO()

        processed_image.save(
            pdf_buffer,
            format="PDF"
        )

        pdf_buffer.seek(0)

        st.download_button(
            label="⬇ Download PDF",
            data=pdf_buffer,
            file_name="scanned_document.pdf",
            mime="application/pdf"
        )

st.markdown("---")
st.caption("Built with Streamlit + Pillow")
