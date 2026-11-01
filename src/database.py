import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import urllib.parse

# Load environment variables from .env file
load_dotenv()

def get_db_engine():
    """
    Creates and returns a SQLAlchemy engine for the Olist MySQL database.
    """
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "olist_ecommerce")
    
    # URL-encode password to handle special characters like '@'
    safe_password = urllib.parse.quote_plus(password)
    
    connection_url = f"mysql+pymysql://{user}:{safe_password}@{host}:{port}/{db_name}"
    engine = create_engine(connection_url)
    return engine