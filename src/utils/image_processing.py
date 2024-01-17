def process_uploaded_invoice_image(uploaded_file):
    """
Processes an uploaded invoice image and prepares it for the model.

Args:
    uploaded_file (FileUploader): The uploaded file object.

Returns:
    list: A list containing a single dictionary with the following keys:
        - "mime_type" (str): The MIME type of the image.
        - "data" (bytes): The raw bytes data of the image.

Raises:
    FileExistsError: If no file is uploaded.
"""
    # Check if an invoice file is uploaded
    if uploaded_file is not None:
        # Get the bytes data from the uploaded file
        bytes_data = uploaded_file.getvalue()

        # Create a list with a dictionary containing image data
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the image
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        # Raise an exception if no file is uploaded
        raise FileNotFoundError("No file uploaded")