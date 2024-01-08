from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as gai

gai.configure(api_key=os.environ.get("API_KEY"))

model = gai.GenerativeModel("gemini-pro-vision")

def get_response(system_role_input, image, user_prompt):
    response = model.generate_content([system_role_input,image[0], user_prompt])
    return response.text