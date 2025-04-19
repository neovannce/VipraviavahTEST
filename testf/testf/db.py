# db.py
import mysql.connector
from mysql.connector import pooling
from config import db_config
import logging

logger = logging.getLogger(__name__)

# Create connection pool
dbconfig = {
    "host": db_config['host'],
    "user": db_config['user'],
    "password": db_config['password'],
    "database": db_config['database'],
    "port": db_config['port'],
    "pool_name": "mypool",
    "pool_size": 5
}

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(**dbconfig)
    logger.info("Database connection pool created successfully")
except Exception as e:
    logger.error(f"Error creating connection pool: {str(e)}")
    connection_pool = None

def get_connection():
    try:
        if connection_pool:
            return connection_pool.get_connection()
        else:
            # Fallback to direct connection if pool creation failed
            return mysql.connector.connect(
                host=db_config['host'],
                user=db_config['user'],
                password=db_config['password'],
                database=db_config['database'],
                port=db_config['port']
            )
    except Exception as e:
        logger.error(f"Error getting database connection: {str(e)}")
        raise
