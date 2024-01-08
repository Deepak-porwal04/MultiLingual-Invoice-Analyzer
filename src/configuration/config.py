from dotenv import load_dotenv
import os

def load_api_key():
    """Loads API key from environment variables."""
    load_dotenv()
    return os.environ.get("API_KEY")
