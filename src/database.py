import sqlite3
from sqlite3 import Error

# Database connection variable
db_connection = None

# Function to establish a database connection
def create_connection():
    global db_connection
    try:
        db_connection = sqlite3.connect(":memory:") # creating a temporary memory database for the purpose of this example
        print(sqlite3.version)
    except Error as e:
        print(e)

# Function to close the database connection
def close_connection():
    global db_connection
    if db_connection:
        db_connection.close()

# Function to execute a query
def execute_query(query):
    global db_connection
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
    except Error as e:
        print(e)

# Function to fetch all rows from a query
def fetch_all(query):
    global db_connection
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(e)

# Function to fetch one row from a query
def fetch_one(query):
    global db_connection
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        return row
    except Error as e:
        print(e)

# Call the function to establish a connection
create_connection()