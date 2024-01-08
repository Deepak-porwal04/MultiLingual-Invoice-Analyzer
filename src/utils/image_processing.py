def process_uploaded_invoice_image(uploaded_file):
    """Processes an uploaded invoice image and prepares it for the model."""
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
