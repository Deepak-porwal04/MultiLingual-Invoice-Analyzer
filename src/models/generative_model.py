import google.generativeai as gai

def initialize_generative_model(model_name):
    """Initializes the Gemini Pro Vision model."""
    model = gai.GenerativeModel(model_name)
    return model

def generate_response_from_invoice_and_query(model,invoice_data, user_query, role_prompt):
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