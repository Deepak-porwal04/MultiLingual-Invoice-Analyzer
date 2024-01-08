from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as gai

gai.configure(api_key=os.environ.get("API_KEY"))

model = gai.GenerativeModel("gemini-pro-vision")

def get_response(system_role_input, image, user_query_prompt):
    response = model.generate_content([system_role_input,image[0], user_query_prompt])
    return response.text

def input_image_processing(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # get the mime type of the image
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileExistsError("No file uploaded")
    
# Streamlit Setup

st.set_page_config(page_title="MultiLingual-Invoice-Analyzer")

st.header("Invoice Analyzer")
user_prompt = st.text_input("Input prompt: ",key='input')
uploaded_file = st.file_uploader("Choose an invoice image: ",type=["jpg","jpeg","png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded invoice",use_column_width=True)

submit = st.button("Analyze the invoice")

system_role = """
You are an expert to understand the invoices in any language.
Based on the given query you have to analyze the invoice and give a correct response of the query.
"""

# if button is clicked

if submit:
    image_data = input_image_processing(uploaded_file)
    response = get_response(system_role,image_data,user_prompt)
    st.subheader("The response is: ")
    st.write(response)