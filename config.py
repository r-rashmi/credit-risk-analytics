import os
from dotenv import load_dotenv

def setup_kaggle_credentials(logger):
    """
    Set up Kaggle credentials from environment variables (.env file).
    
    Args:
        logger: Logger instance to use for logging messages
    """
    logger.info("Setting up Kaggle credentials from environment variables...")
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get credentials from .env file
    username = os.getenv("KAGGLE_USERNAME")
    api_key = os.getenv("KAGGLE_KEY")
    
    if username and api_key:
        logger.info("✅ Successfully loaded Kaggle credentials from environment variables")
        return username, api_key
    
    # Credentials not found, raise error
    logger.error("❌ Kaggle credentials not found in environment variables!")
    raise FileNotFoundError("Kaggle credentials not found in .env file.")