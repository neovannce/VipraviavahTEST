# config.py
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Secret key for session management
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Database configuration
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'vipravivaah')
DB_PORT = os.environ.get('DB_PORT', '3306')

# Log the configuration (without sensitive data)
logger.info(f"Database configuration loaded:")
logger.info(f"Host: {DB_HOST}")
logger.info(f"Database: {DB_NAME}")
logger.info(f"Port: {DB_PORT}")

db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME,
    'port': int(DB_PORT)
}
