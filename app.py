import streamlit as st
import os
from PIL import Image
import google.generativeai as gai
from dotenv import load_dotenv

# 1. Load API key and model ───────────────────────────────────────────────────────
# Load the API key from environment variables
load_dotenv()
gai.configure(api_key=os.environ.get("API_KEY"))

# Initialize the generative model
model = gai.GenerativeModel("gemini-pro-vision")

# 2. Define functions for invoice processing and response generation ─────────────
def generate_response_from_invoice_and_query(invoice_data, user_query, role_prompt):
    """Generates a response to a user query based on the provided invoice image and role prompt.

    Args:
        invoice_data: A list containing a dictionary with image data (mime_type and data).
        user_query: The user's query prompt.
        role_prompt: A prompt describing the system's role and capabilities.

    Returns:
        The generated response text.
    """

    response = model.generate_content([role_prompt, invoice_data[0], user_query])
    return response.text

def process_uploaded_invoice_image(uploaded_file):
    """Processes an uploaded invoice image and prepares it for the model.

    Args:
        uploaded_file: The uploaded file object.

    Returns:
        A list containing a dictionary with image data (mime_type and data).

    Raises:
        FileExistsError: If no file is uploaded.
    """

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the image
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileExistsError("No file uploaded")

# 3. Set up Streamlit interface ─────────────────────────────────────────────────
st.set_page_config(page_title="Multilingual Invoice Analyzer")

st.header("Invoice Analyzer")

# 4. Get user input and display uploaded image ──────────────────────────────────
user_query = st.text_input("Enter your query about the invoice:", key='input')
uploaded_invoice = st.file_uploader("Upload invoice image:", type=["jpg", "jpeg", "png"])

if uploaded_invoice is not None:
    invoice_image = Image.open(uploaded_invoice)
    st.image(invoice_image, caption="Uploaded invoice", use_column_width=True)

# 5. Define system role prompt ─────────────────────────────────────────────────
system_role = """
I am an expert in understanding invoices in various languages. 
I will carefully analyze the invoice and provide accurate responses to your queries.
Feel free to ask me anything about the invoice, such as:
- Total amount due
- Invoice date
- Vendor information
- Specific line items
- Payment terms
- Tax details
- Any other relevant information
"""

# 6. Handle user interaction and generate response ─────────────────────────────
if st.button("Analyze Invoice"):
    with st.spinner("Processing invoice..."):  # Replace with st.empty for custom progress bar
        try:
            invoice_data = process_uploaded_invoice_image(uploaded_invoice)
            response = generate_response_from_invoice_and_query(invoice_data, user_query, system_role)
            st.subheader("Response:")
            st.write(response)
        except FileExistsError as e:
            st.error(e)