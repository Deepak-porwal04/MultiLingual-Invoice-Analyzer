import google.generativeai as gai

def initialize_generative_model(model_name):
    """
    Initializes a generative model using the specified model name.

    Args:
        model_name (str): The name of the generative model to initialize.

    Returns:
        gai.GenerativeModel: The initialized model instance.

    Raises:
        ImportError: If the `google.generativeai` module is not found.
    """
    model = gai.GenerativeModel(model_name)
    return model

def generate_response_from_invoice_and_query(model, invoice_data, user_query, role_prompt):
    """Generates a response to a user query based on the provided invoice image and role prompt.

    Args:
        model (gai.GenerativeModel): The initialized generative model.
        invoice_data: A list containing a dictionary with image data (mime_type and data).
        user_query (str): The user's query about the invoice.
        role_prompt (str): A prompt that guides the model's response based on a specific role.

    Returns:
        The generated response text.
    """

    response = model.generate_content([role_prompt, invoice_data[0], user_query])
    # Extract and return the response text
    return response.text