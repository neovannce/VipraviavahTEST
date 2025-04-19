# db.py
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import os
import logging

logger = logging.getLogger(__name__)

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=int(os.environ.get('DB_PORT', '3306'))
        )
        return connection
    except mysql.connector.Error as err:
        logger.error(f"Error connecting to database: {err}")
        raise
