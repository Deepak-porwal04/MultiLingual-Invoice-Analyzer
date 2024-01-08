from dotenv import load_dotenv
import os

def load_api_key():
    """
   Loads the API key from the .env file.

   Loads the .env file using the `load_dotenv` function, then retrieves
   the API key stored in the "API_KEY" environment variable.

   Returns:
       str: The API key value, or None if the key is not found.
   """
    load_dotenv()
    return os.environ.get("API_KEY")
