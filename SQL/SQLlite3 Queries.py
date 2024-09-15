import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER)''')

    # Insert data into the table
    cursor.execute("INSERT INTO users (name, age) VALUES ('Jerry', 62)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Grace', 67)")

    # Select all data from the table
    cursor.execute("SELECT DISTINCT name, age FROM users")
    data = cursor.fetchall()

    # Print the fetched data
    print(data)

    # Commit the transaction
    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed
    if conn:
        conn.close()
        
