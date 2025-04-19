# config.py
import os

# Secret key for session management
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Database configuration
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'vipravivaah')

db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME,
    'port': int(os.getenv('DB_PORT', 19861))
}
