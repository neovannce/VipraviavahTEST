# db.py
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_connection():
    try:
        # Log the connection attempt with masked credentials
        logger.info(f"Attempting to connect to database at {DB_HOST}:{os.environ.get('DB_PORT', '3306')}")
        logger.info(f"Using database: {DB_NAME}")
        
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=int(os.environ.get('DB_PORT', '3306')),
            connect_timeout=10  # Add connection timeout
        )
        logger.info("Database connection successful")
        return connection
    except mysql.connector.Error as err:
        logger.error(f"Database connection error: {str(err)}")
        logger.error(f"Error code: {err.errno}")
        logger.error(f"SQL state: {err.sqlstate}")
        logger.error(f"Error message: {err.msg}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during database connection: {str(e)}")
        raise
