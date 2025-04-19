# config.py
import os

db_config = {
    'host': os.getenv('DB_HOST', 'mysql-385e1d9b-shivankar-b189.b.aivencloud.com'),
    'user': os.getenv('DB_USER', 'avnadmin'),
    'password': os.getenv('DB_PASSWORD', 'AVNS_IWNnIqNtr9DjL3mVLgW'),
    'database': os.getenv('DB_NAME', 'shivankar'),
    'port': int(os.getenv('DB_PORT', 19861))
}

SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
