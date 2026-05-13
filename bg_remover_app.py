import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Background Remover",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ AI Background Remover")
st.write("Upload an image and remove the background instantly.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    input_image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(input_image, use_container_width=True)

    if st.button("Remove Background"):

        with st.spinner("Removing background..."):

            # Convert image to bytes
            input_bytes = uploaded_file.read()

            # Remove background
            output_bytes = remove(input_bytes)

            # Convert output to image
            output_image = Image.open(BytesIO(output_bytes))

        st.subheader("Background Removed")
        st.image(output_image, use_container_width=True)

        st.download_button(
            label="⬇ Download PNG",
            data=output_bytes,
            file_name="background_removed.png",
            mime="image/png"
        )

st.markdown("---")
st.caption("Built with Streamlit + rembg")
