import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='config/.env')

def get_config(key, default=None):
    """Fetch the configuration value for the given key."""
    return os.getenv(key, default)
