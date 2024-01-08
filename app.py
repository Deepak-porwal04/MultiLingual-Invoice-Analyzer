import streamlit as st
import google.generativeai as gai
from PIL import Image
from src.configuration import config
from src.models import generative_model
from src.utils import prompts,image_processing

# Load API key
api_key = config.load_api_key()
gai.configure(api_key=api_key)

# Initialize model
model = generative_model.initialize_generative_model("gemini-pro-vision")

# Streamlit setup
st.set_page_config(page_title="Multilingual Invoice Analyzer")
st.header("Invoice Analyzer")

# User input
user_query = st.text_input("Enter your query about the invoice:", key='input')
uploaded_invoice = st.file_uploader("Upload invoice image:", type=["jpg", "jpeg", "png"])

if uploaded_invoice is not None:
    invoice_image = Image.open(uploaded_invoice)
    st.image(invoice_image, caption="Uploaded invoice", use_column_width=True)

# Handle user interaction and generate response
if st.button("Analyze Invoice"):
    with st.spinner("Processing invoice..."):  # Replace with st.empty for custom progress bar
        try:
            invoice_data = image_processing.process_uploaded_invoice_image(uploaded_invoice)
            response = generative_model.generate_response_from_invoice_and_query(model,invoice_data, user_query, prompts.system_role)
            st.subheader("Response:")
            st.write(response)
        except FileExistsError as e:
            st.error(e)