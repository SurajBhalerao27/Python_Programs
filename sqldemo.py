import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

def create_table(conn):
    """Create a table in the SQLite database"""
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                age INTEGER,
                                email TEXT
                            );"""
        conn.execute(sql_create_table)
        print("Table 'users' created successfully")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def insert_data(conn, user):
    """Insert a new row into the users table"""
    sql_insert = """INSERT INTO users (name, age, email) VALUES (?, ?, ?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql_insert, user)
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def fetch_data(conn):
    """Fetch all rows from the users table"""
    sql_select = "SELECT * FROM users"
    try:
        cur = conn.cursor()
        cur.execute(sql_select)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error: {e}")

def main():
    database = "Demo.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    # Create a new table
    if conn is not None:
        create_table(conn)
        
        # Insert data into the table
        user_1 = ('John Doe', 30, 'john.doe@example.com')
        user_2 = ('Jane Doe', 25, 'jane.doe@example.com')
        insert_data(conn, user_1)
        insert_data(conn, user_2)
        
        # Fetch data from the table
        fetch_data(conn)
        
        # Close the connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
