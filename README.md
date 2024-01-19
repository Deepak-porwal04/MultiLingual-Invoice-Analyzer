# Multilingual Invoice Analyzer

## Overview

This project enables users to analyze invoice images in various languages and extract relevant information by asking natural language questions. It leverages the power of Google's Gemini Pro Vision model for image understanding and text generation, providing a user-friendly interface through a Streamlit app.

## Table of Contents

- [Features](#key-features)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#Usage)

## Key Features
- **Multilingual invoice analysis**: Handles invoices in multiple languages with the help of Gemini Pro Vision.
- **Question answering**: Users can ask diverse questions about invoice details.
- **Streamlit interface**: Simple and interactive web interface for easy usage.
- **Prompt-based guidance**: Uses prompts to define the system's role and capabilities, directing the model's responses effectively.


## Installation

1. Clone this repository:
  ```bash
  git clone https://github.com/Deepak-porwal04/MultiLingual-Invoice-Analyzer.git
  ```

2. Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```
3. Set up the environment variables:

 - Create a `.env` file in the project root directory.

- Add your Gemini API key to the `.env` file:
```bash
API_KEY=your_gemini_api_key
  ```
4. Run the Streamlit application:
  ```
  streamlit run app.py
  ```

## Prerequisites

- `python>=3.9`: Designed using python 3.9 
- `streamlit`: Streamlit library for building web applications.
- `google.generativeai`: Gemini API for generative models.
- `python-dotenv`: To store the environment variables secretly  

## Usage

1. Open the application in your browser.
2. Enter your query about the invoice in the provided text input.
3. Upload an invoice image (in JPG, JPEG, or PNG format).
4. Click the "Analyze Invoice" button.
5. The system will process the invoice and provide a response based on the query.