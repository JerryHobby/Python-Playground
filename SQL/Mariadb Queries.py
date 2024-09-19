import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import logging
# Load environment variables from .env file
logging.basicConfig(level=logging.DEBUG)

load_dotenv()


# Database connection variables
hostname = os.getenv('HOSTNAME')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
logging.debug(f"Hostname: {hostname}, User: {user}, Database: {database}")

try:
    # Connect to the MariaDB database
    conn = mysql.connector.connect(
        host=hostname,
        user=user,
        password=password,
        database=database
    )

    if conn.is_connected():
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users2 (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            age INT)''')

        # Insert data into the table
        cursor.execute("INSERT INTO users2 (name, age) VALUES ('Jerry', 62)")
        cursor.execute("INSERT INTO users2 (name, age) VALUES ('Grace', 67)")

        # Select all data from the table
        cursor.execute("SELECT DISTINCT name, age FROM users2")
        data = cursor.fetchall()

        # Print the fetched data
        print(data)

        # Commit the transaction
        conn.commit()

except Error as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed
    if conn.is_connected():
        cursor.close()
        conn.close()